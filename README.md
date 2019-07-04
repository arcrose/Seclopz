# Seclopz

Seclopz is a service designed to facilitate security operations at Mozilla.
Note that this is not an official Mozilla project- it is a side project
developed during my own personal time allowed for working on such projects at
work.  As such, it may not support many features that someone may expect such a
tool to have.  I am developing it incrementally to solve specific problems one
at a time.

## Features

Features that have been implemented or are planned for development are
described in `docs/features.md`.  This document also explains the expected
use cases for each feature.  Many of Seclopz's features tie heavily into
[MozDef](https://github.com/mozilla/mozdef) and
[Person API](https://github.com/mozilla-iam/cis/blob/master/docs/PersonAPI.md).

## Project Layout

The top-level `docs/` directory contains global documentation including high-level
design documents such as the relational diagram for the API's database schema,
specification documents and everything else explaining Seclopz as a cohesive
whole.

`seclopzapi/` contains everything pertaining specifically to the API component
of Seclopz.  This includes things like
  * `seclopzapi/README.md` explains the setup and usage of the API.
  * `seclopzapi/docs` that describes the API endpoints and common workflows.
  * `seclopzapi/seclopzapi` contains the application code for the API.
  * `seclopzapi/tests` contains tests for the API component.

Likewise, `seclopzbot/` contains everything pertaining specifically to the
Slack Bot component of Seclopz.  This includes
  * `seclopzbot/README.md` explains the setup and usage of the bot.
  * `seclopzbot/docs` that describes the bot's command interface.
  * `seclopzbot/seclopzbot` contains the application code for the bot.
  * `seclopzbot/tests` contains tests for the bot component.

## Development

The Seclopz API is built on the [Flask](http://flask.pocoo.org/) web micro-
framework.

The Seclopz bot uses [Slack's Real Time Messaging](https://api.slack.com/rtm)
(RTM) API.

Documentation is compiled into a static site using
[MkDocs](https://www.mkdocs.org/).

## Contributing

If you would like to contribute to the development of Seclopz, you will be
expected to conform to Mozilla's [Community Participation Guidelines](
https://www.mozilla.org/en-US/about/governance/policies/participation/).
See the [CODE_OF_CONDUCT.md]() file for more information.

Discussion takes place in the `#seclopz` channel of Mozilla's Slack workspace,
which requires that you agree to our
[Non-Disclosure Agreement](https://wiki.mozilla.org/NDA) to join.

You are also welcome to open issues to ask questions, report issues and start
discussions about features.
