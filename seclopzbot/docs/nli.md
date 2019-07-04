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

## Descriptions

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
