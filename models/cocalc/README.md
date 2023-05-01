# CoCalc

![Logo](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXg6qfOLc9AMYixqDnvASg1Hpjpq-AYmBDqQ&usqp=CAU)

CoCalc is a cloud-based collaborative software oriented towards research, teaching, and scientific publishing purposes. It uses the GPT-3.5-Turbo and that's why it was added to the project, besides being easy to use.

## Cookies? Relax.

Many projects ask you to get the page's cookies and use them in a variable. But you don't have to! You just need to generate a `uuid` and put it as `CC_ANA`.

![Cookie Illustrator](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRkNYtl15cTPNlGlEKK1qc9YsUMLZbfnx9Dqw&usqp=CAU)

## Problems

Unfortunately it's slow, but that's because it doesn't use `text/event-stream`. Which is a type used to send already processed chunks of content to the client, instead it gets everything and then sends it all at once. So if you order something big it might take a while to ship.
