'''Exports a `Transition` class that describes a transition between two states
that a `Command`'s `Parser` can be in.
'''

from dataclasses import dataclass, field
from enum import Enum
import re
from typing import List, Optional, Tuple


class MatchRule(Enum):
    '''Enumerates all of the possible rules for matching against an input
    and stack values.
    '''

    CHECK_NONE = 0
    TEXT_ONLY = 1
    STACK_ONLY = 2
    TEXT_AND_STACK = 3


class StackOperation(Enum):
    '''Enumerates all of the allowed operations on a stack.
    '''

    NONE = 0
    PUSH = 1
    POP = 2
    POP_THEN_PUSH = 3


@dataclass
class Transition:
    '''Describes a possible transition that can occur between two states.

        * `fr` is the symbol for the state from which the transition can
        occur.
        * `to` is the symbol for the state to which the transition occurs.
        * `match` is an optional regular expression applied to an input token to
        determine whether to apply the transition.
        * `stack_match` is an optional symbol that can be matched against the
        top item of the stack to determine whether to apply the transition.
        * `param` is an optional symbol that, when provided, will be used to
        tag a new item to be placed on the stack along with the input token.
        * `pop` is an optional boolean that, when `True` will result in the top
        item of the stack being popped if the transition is followed.

    When both `match` and `stack_match` are `None`, the transition rule will
    apply if the input token provided is `None`.

    When `param` is provided, `match` is disregarded.  The transition will be
    applied if `stack_match` is not present or it matches the symbol tagging
    the top item of the stack.  When a `param` transition is applied, the
    input token will be tagged with the symbol given to `param` and pushed onto
    the top of the stack.

    When both `param is not None` and `pop == True`, then the top item of the
    stack will be replaced with the new param value tagged with the symbol
    `param` is set to.
    '''

    fr: str
    to: str
    match: Optional[str] = field(default=None)
    stack_match: Optional[str] = field(default=None)
    param: Optional[str] = field(default=None)
    pop: bool = field(default=False)


    def _determine_rules(self) -> Tuple[MatchRule, StackOperation]:
        match_rule = {
            (True, False): MatchRule.TEXT_ONLY,
            (False, True): MatchRule.STACK_ONLY,
            (True, True): MatchRule.TEXT_AND_STACK,
            (False, False): MatchRule.CHECK_NONE
        }[(self.match is not None, self.stack_match is not None)]

        stack_op = {
            (True, False): StackOperation.PUSH,
            (False, True): StackOperation.POP,
            (True, True): StackOperation.POP_THEN_PUSH,
            (False, False): StackOperation.NONE
        }[(self.param is not None, self.pop)]

        return (match_rule, stack_op)

    
    def _matches(
            self,
            state: str,
            rule: MatchRule,
            top_stack_sym: Optional[str],
            tkn: Optional[str]) -> bool:

        state_matches = state == self.fr

        if self.match is None:
            text_matches = False
        else:
            pattern = re.compile(self.match)
            text_matches = tkn is not None and pattern.match(tkn) is not None

        if self.stack_match is None:
            stack_matches = False
        else:
            pattern = re.compile(self.stack_match) if have_s_match else None
            stack_matches = top_stack_sym is not None and\
                    stk_pattern.match(top_stack_sym) is not None

        any_rule_applies = any([
            rule == MatchRule.CHECK_NONE and tkn is None,
            rule == MatchRule.TEXT_ONLY and text_matches,
            rule == MatchRule.STACK_ONLY and stack_matches,
            rule == MatchRule.TEXT_AND_STACK and text_matches and stack_matches
        ])

        return state_matches and any_rule_applies


    def _apply_stack_operation(
            self,
            stack: List[Tuple[str, str]],
            op: StackOperation,
            value: Optional[str] = None) -> bool:
        # Note: `None` is a valid value for a parameter to take. We either
        # parsed out a string parameter value or we did not where we expected
        # one.  The latter case must be recognized for the parser's use.
        # Therefore we do not check that `value is not None`.
        have_param = self.param is not None
        not_empty = len(stack) > 0

        if op == StackOperation.NONE:
            return True

        if op == StackOperation.PUSH and have_param:
            stack.append((self.param, value))
            return True

        if op == StackOperation.POP and not_empty:
            stack.pop()
            return True

        if op == StackOperation.POP_THEN_PUSH and not_empty and have_param:
            stack.pop()
            stack.append(self.param)
            return True

        return False


    def apply(
            self,
            state: str,
            stack: List[Tuple[str, str]],
            token: Optional[str]) -> Optional[str]:
        '''Apply a transition rule to a stack and input token.

        `state` is the symbol representing the current state.

        The `stack` is expected to be a list of tagged parameters, created by
        instances of `Transition`.  Each `(str, str)` pair is a
        `(self.param, token)` where `token` can be `None`.

        The `token` argument is the next input token from a user's input
        command.  In cases where we may want to indicate that an invalid token
        was encountered, the `token` can be `None`.

        This function returns the next state symbol for the parser to move to.

        If no inputs match, `None` will be returned, indicating that the
        transition was not followed.

        If the `Transition` is configured in such a way that it could not be
        applied in any meaningful way, `None` will be returned.  For example,
        if `pop == True and len(stack) == 0`.
        '''
        (match_rule, stack_op) = self._determine_rules()
        top_symbol = stack[0][0] if len(stack) > 0 else None

        does_match = self._matches(state, match_rule, top_symbol, token)

        if does_match:
            did_op = self._apply_stack_operation(stack, stack_op, token)
            return self.to if did_op else None

        return None
