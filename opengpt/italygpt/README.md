# ItalyGPT

![Logo](https://italygpt.it/static/logo.png)

ItalyGPT is an italian website, giving access to gpt for italians when ChatGPT was banned in Italy and now giving access to gpt3.5-turbo for free and gpt4 cheaper than OpenAI.

[How to Use](https://github.com/uesleibros/OpenGPT/tree/main/models/italygpt/DOC.md)

## Problems

Unfortunately it's slow, but that's because it doesn't use `text/event-stream`. Which is a type used to send already processed chunks of content to the client, instead it gets everything and then sends it all at once. So if you order something big it might take a while to ship.
