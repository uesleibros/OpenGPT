# How to Use

To use this model is very simple, first you need to import it:

```py

from models.you.model import Model

```

After importing, we initialize the class to work with it.

```py

you = Model()

```


Now we define in the `SetupConversation` function what we want to ask.

```py

you.SetupConversation("prompt here")

```

> **Attention:** You can pass the history to the artificial intelligence to remember what you said. You can make the memory (`history`) dynamic if you like, adding to the list whenever you return the answer.
for example:

```py
you.SetupConversation("prompt here", history=[{"question": "Hello! my favorite color is Blue.", "answer": "Yes, i will remember this."}])
```


Now we just run the `SendConversation` function to get the answer.

```py

print(you.SendConversation().answer)

```

The complete code would be like this:

```py

from models.you.model import Model

chat = []
you = Model()

you.SetupConversation("Create an list with all popular cities of United States.", history=chat)

res = you.SendConversation()

chat.append({"question": res.prompt, "answer": res.answer})

print(res.answer)
```
