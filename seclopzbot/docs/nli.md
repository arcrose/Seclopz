# Natural Language Interface

Commands are descrined as parametized structured sentences.  Imagine a command
line interface invocation such as the following.

```
cargo new --bin --edition 2018 --name my_project
```

One could imagine translating this into an English sentence such as

> Cargo, create a new binary project using Rust 2018 called my_project.

We may represent that here as

```
cargo (...) new [binary | lib] [using [Rust | edition] <edition>] (called | named) <name>
```

## Documentation

For the purposes of documenting commands supported by Seclopzbot, the following
conventions will be used.

  1. All commands will start with the word `seclopzbot`.
  2. All punctuation is ignored.
  3. Where room exists in a command for arbitrary text, `(...)` is used.
  4. Required words are not annotated, e.g. in `seclopzbot new hire`.
  5. Where more than one word/sequence of words are allowed, `|` separates
  acceptable options as in `seclopzbot (hello | hi | hey there)`.
  6. Optional sequences of words are enclosed in square brackets as in
  `seclopzbot start [a new | an] investigation`.
  7. Parameters are enclosed in angle brackets as in
  `seclopzbot close <investigation>`
  8. Parameters that match multiple words can appear at the end of a command
  and are suffixed with elipses as in
  `seclopzbot add note to <investigation> <words...>`.

## Implementation

Seclopzbot's natural language interface is implemented using a relatively
simple [deterministic pushdown automaton](
https://en.wikipedia.org/wiki/Pushdown_automaton).  Because Seclopzbot only
has to be able to handle fairly small sets of acceptable inputs and isn't
concerned with the grammatical structure of a command, describing commands
registered by the bot only requires that an author define:

1. The name of the command.
2. A help string describing the command.
3. A format description illustrating the expected input format.
4. A callback function to invoke with any parameters parsed.
5. A parser specification described as
  1. A start state symbol.
  2. A finished state symbol.
  3. A list of states symbols.
  5. A list of transitions that will be tested in the order listed.

All the magic happens in the `Transition`s, which allow you to specify:

  * The start state to which they apply.
  * The state to which the parser moves if input matches.
  * A regular expression that can match a single word.
  * A symbol to match against that of the top of the current stack.
  * Whether the text matched is a parameter and a tag to associate with the
  string parsed when it is pushed onto the stack.
