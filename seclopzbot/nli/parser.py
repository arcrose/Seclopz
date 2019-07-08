'''Exports a `Parser` class that describes a parser capable of determining
whether an input string processed as a list of tokens (words) matches an
expected `Command` format.
'''

from dataclasses import dataclass
from typing import List

from nli.transition import Transition


@dataclass
class Parser:
    '''Contains all of the necessary parts to describe how to parse an input
    string that invokes a `Command`.
    
        * `start` is the symbol for the state the parser starts in.
        * `end` is the symbol for the state the parser ends in successful
        termination in.
        * `states` is a list of symbols, one for each state the parser can
        enter.
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
    states: List[str]
    transitions: List[Transition]


    def parse(self, input_str: str) -> List[str]:
        '''Parse an input string into tokens and then run it through a
        deterministic pushdown automaton to extract a list of parameters to
        a command callback.
        '''

        return []
