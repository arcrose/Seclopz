# Seclopzbot Commands

Seclopzbot provides a simple [Natural Language User Interface](
https://en.wikipedia.org/wiki/Natural-language_user_interface), (NLI)
facilitating instruction processing in a semi-conversational fashion.

See the [Natural Language Interface](seclopzbot/docs/nli.md) document for
a specification describing how these commands are implemented.

## Supported Commands

Below is a list of the commands Seclopzbot supports.

### Information for new hires

When a new hire joins Mozilla, they are asked to follow a brief guide
informing them of common and best practices around securing accounts and
communications at Mozilla.  Seclopzbot will respond to a link to this guide
when requested.

```
seclopzbot (...) new hire[s] (...)
```

**Examples**

```
seclopzbot hi! I'm a new hire.

seclopzbot is there a guide for new hires?
```
