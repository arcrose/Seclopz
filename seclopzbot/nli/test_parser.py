import unittest

from nli.parser import Parser, ParseError
from nli.transition import Transition


class ParserTests(unittest.TestCase):
    def test_parsing_succeeds_if_end_state_reached(self):
        p = Parser(
                start='start',
                end='end',
                transitions=[
                    Transition(fr='start', to='next', match='test1'),
                    Transition(fr='start', to='end', match='test'),
                    Transition(fr='start', to='other', match='test')
                ])

        args = p.parse('test')
        assert len(args) == 0


    def test_parsing_fails_if_end_state_not_reached(self):
        p = Parser(
                start='start',
                end='end',
                transitions=[
                    Transition(fr='start', to='other', match='test')
                ])

        self.assertRaises(ParseError, p.parse, 'test')


    def test_parsing_fails_if_no_transition_applies(self):
        p = Parser(
                start='start',
                end='end',
                transitions=[
                    Transition(fr='start', to='end', match='test')
                ])

        self.assertRaises(ParseError, p.parse, 'invalid')


    def test_simple_param_extraction(self):
        p = Parser(
                start='start',
                end='end',
                transitions=[
                    Transition(fr='start', to='greet', match='hi'),
                    Transition(fr='greet', to='greet', match='Im'),
                    Transition(fr='greet', to='end', match='.*', param='name')
                ])
                
        args = p.parse('hi I\'m tester')
        assert 'name' in args and args['name'] == 'tester'


    def test_complex_param_extraction(self):
        # cargo new [binary | lib] [using [rust | edition] <edition>]
        # (called | named) <name>
        p = Parser(
                start='start',
                end='end',
                transitions=[
                    Transition(fr='start', to='cargo', match='cargo'),
                    Transition(fr='cargo', to='new', match='new'),
                    Transition(fr='new', to='binlib', match='(binary|lib)'),
                    Transition(fr='new', to='using', match='using'),
                    Transition(fr='new', to='called', match='(called|named)'),
                    Transition(fr='binlib', to='using', match='using'),
                    Transition(fr='using', to='edition', match='(Rust|edition)'),
                    Transition(fr='edition', to='called', match='\d{4}', param='edition'),
                    Transition(fr='called', to='name', match='(called|named)'),
                    Transition(fr='name', to='end', match='.*', param='name')
                ])

        valid_inputs = [
            'cargo new called test',
            'cargo new binary called test',
            'cargo new lib called test',
            'cargo new using 2018 called test',
            'cargo new binary using 2018 named test',
            'cargo new lib using Rust 2018 named test',
            'cargo new lib using edition 2018 called test'
        ]

        for input_ in valid_inputs:
            args = p.parse(input_)
            edition = args.get('edition')

            assert edition is None or edition == '2018'
            assert 'name' in args and args['name'] == 'test'
    
    
    def test_complex_param_extraction(self):
        # cargo new [binary | lib] [using [rust | edition] <edition>]
        # (called | named) <name>
        p = Parser(
                start='start',
                end='end',
                transitions=[
                    Transition(fr='start', to='cargo', match='cargo'),
                    Transition(fr='cargo', to='new', match='new'),
                    Transition(fr='new', to='binlib', match='(binary|lib)'),
                    Transition(fr='new', to='using', match='using'),
                    Transition(fr='new', to='called', match='(called|named)'),
                    Transition(fr='binlib', to='using', match='using'),
                    Transition(fr='using', to='edition', match='(Rust|edition)'),
                    Transition(fr='edition', to='called', match='\d{4}', param='edition'),
                    Transition(fr='called', to='name', match='(called|named)'),
                    Transition(fr='name', to='end', match='.*', param='name')
                ])

        invalid_inputs = [
            'cargo called test',
            'cargo new test',
            'cargo new lib test',
            'cargo new 2018 called test',
            'cargo new binary using 2018 named test',
            'cargo new using 2018 test',
        ]

        for input_ in invalid_inputs:
            self.assertRaises(ParseError, p.parse, input_)
