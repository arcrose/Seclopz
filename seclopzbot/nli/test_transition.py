import unittest

from nli.transition import Transition


class TransitionTests(unittest.TestCase):
    def test_matching_transition_applied(self):
        t = Transition(fr='start', to='end', match='test')
        state = 'start'
        stack = []
        token = 'test'

        assert t.apply(state, stack, token) == 'end'


    def test_ignored_if_no_match(self):
        t = Transition(fr='start', to='end', match='testing')
        state = 'start'
        stack = []
        token = 'test'

        assert t.apply(state, stack, token) is None


    def test_matching_on_both_input_and_stack(self):
        t = Transition(
                fr='start', to='end', match='test', stack_match='t')
        state = 'start'
        stack = [('t', 'value')]
        token = 'test'

        assert t.apply(state, stack, token) == 'end'


    def test_match_on_input_required(self):
        t = Transition(
                fr='start', to='end', match='test', stack_match='t')
        state = 'start'
        stack = [('t', 'value')]
        token = 'invalid'

        assert t.apply(state, stack, token) is None


    def test_match_on_stack_required(self):
        t = Transition(
                fr='start', to='end', match='test', stack_match='t')
        state = 'start'
        stack = [('x', 'value')]
        token = 'test'

        assert t.apply(state, stack, token) is None


    def test_stack_push(self):
        t = Transition(fr='start', to='end', match='test', param='t')
        state = 'start'
        stack = []
        token = 'test'

        t.apply(state, stack, token)
        assert len(stack) == 1 and stack[0] == ('t', 'test')


    def test_stack_pop(self):
        t = Transition(fr='start', to='end', match='test', pop=True)
        state = 'start'
        stack = [('x', 'value')]
        token = 'test'

        t.apply(state, stack, token)
        assert len(stack) == 0


    def test_pop_ignored_if_stack_empty(self):
        t = Transition(fr='start', to='end', match='test', pop=True)
        state = 'start'
        stack = []
        token = 'test'

        assert t.apply(state, stack, token) is None
        assert len(stack) == 0


    def test_pop_before_push(self):
        t = Transition(fr='start', to='end', match='test', pop=True, param='t')
        state = 'start'
        stack = [('x', 'value')]
        token = 'test'

        assert t.apply(state, stack, token) == 'end'
        assert len(stack) == 1 and stack[0] == ('t', 'test')

