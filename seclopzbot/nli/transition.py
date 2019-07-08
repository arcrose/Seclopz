'''Exports a `Transition` class that describes a transition between two states
that a `Command`'s `Parser` can be in.
'''

from dataclasses import dataclass, field
from typing import Optional


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
        * `paramis an optional symbol that, when provided, will be used to
        tag a new item to be placed on the stack along with the input token.
        * `pop` is an optional boolean that, when `True` will result in the top
        item of the stack being popped if the transition is followed.

    When both `match` and `stack_match` are `None`

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
