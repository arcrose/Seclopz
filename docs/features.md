# Seclopz Features

## Table of Contents

* [Natural Language Interface](#natural-language-interface)
* [Investigations](#investigations)
  * [Investigation Context Management](#investigation-context-management)
    * [Supported Contexts](#supported-contexts)

## Natural Language Interface

For a list of commands supported by seclopzbot, see
`seclopzbot/docs/commands.md`.

The Slack bot component of Seclopz can interpret (English only) natural language
commands similar to Slack's own slackbot.

## Investigations

Features pertaining to investigations are designed to assist security engineers
with carrying out investigations.  This includes creating, adding notes and
references to evidence about and modifying the status of an investigation in
MozDef.

### Investigation Context Management

While an investigation is underway, security engineers frequently have to keep
organizational information in their heads related to things like people taking
time off of work, traveling and so on.  So, for example, if a
[GeoModel](https://github.com/mozilla/geomodel) alert is detected indicating
that someone has logged into Mozilla services from an unexpected origin,
Seclopz can be informed of this fact.  Having these pieces of awareness
allow Seclopz to automate certain common tasks like pining users to ask if they
are traveling and automatically acknowledging alerts for users that are known
to be traveling or using a VPN.

#### Supported Contexts

No contexts are supported at this time.
