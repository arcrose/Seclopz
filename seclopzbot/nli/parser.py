'''Exports a `Parser` class that describes a parser capable of determining
whether an input string processed as a list of tokens (words) matches an
expected `Command` format.
'''

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

from nli.transition import Transition


class ParseError(Exception):
    def __init__(
            self,
            state: str,
            stack: List[(str, str)],
            tokens: List[Optional[str]]):
        self.state = state
        self.stack = stack
        self.tokens = tokens

        super().__init__(f'''
Parser state:
    state symbol = {state}
    stack = {stack}
    tokens = {tokens}
''')


@dataclass
class Parser:
    '''Contains all of the necessary parts to describe how to parse an input
    string that invokes a `Command`.
    
        * `start` is the symbol for the state the parser starts in.
        * `end` is the symbol for the state the parser ends in successful
        termination in.
        * `transitions` is a list of `Transition`s describing inputs to match
        against, states to transition to & from and how to manipulate the
        stack.

    A `Parser` will terminate in failure if and only if one of the following
    conditions are met:

        1. All input is processed and the end state has not been reached.
        2. Input is encountered for which no transition applies, given the
        current state and top of the stack.
    '''

    start: str
    end: str
    transitions: List[Transition]


    def _tokenize(self, input_: str) -> List[Optional[str]]:
        words = filter(
            lambda word: len(word) > 0,
            input_.split(' '))

        cleaned = map(
            # Filter punctuation from each word.
            lambda word: str(
                filter(
                    lambda c: c not in string.punctuation,
                    word)),
            words)

        return list(filter(lambda tkn: len(tkn) > 0, cleaned))


    def _transition(
            self,
            state: str,
            stack: List[(str, str)],
            tkn: Optional[str]) -> Optional[str]:
        for tx in self.transitions:
            next_state = tx.apply(state, stack, tkn)

            if next_state is not None:
                return next_state

        return None


    def parse(self, input_str: str) -> Dict[str, Optional[str]]:
        '''Parse an input string into tokens and then run it through a
        deterministic pushdown automaton to extract a tagged set of parameters.

        Inputs are tokenized by splitting on the space character (`' '`).  Each
        resulting word then has all English punctuation (`string.punctuation`)
        removed.

        A `ParseError` will be raised if the parser never enters the `end`
        `state` after processing all input tokens.  Once all the tokens have
        been exhausted, transition rules will be tested with inputs of `None`
        until either no transition applies until no rule applies.
        '''

        state = self.start
        stack = []
        tokens = self._tokenize(input_str)

        for tkn in tokens:
            next_state = self._transition(state, stack, tkn)

            if next_state is not None:
                state = next_state

        while next_state is not None and next_state != self.end:
            next_state = self._transition(state, stack, None)

        if next_state != self.end:
            raise ParseError(state, stack, tokens)

        return dict(stack)
