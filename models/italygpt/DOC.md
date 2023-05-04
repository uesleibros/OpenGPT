# How to Use

To use this model is very simple, first you need to import it:

```py
from models.italygpt.model import Model
```

After importing, we initialize the class to work with it.

```py
italygpt = Model()
```

Now we just run the `GetAnswer` function to get the answer.

```py
print(italygpt.GetAnswer(prompt="What is the meaning of life?").answer)
```
Note: The answer is html formatted.

If you want to keep conversations, when calling the GetAnswer method pass the messages parameter.

```py
print(italygpt.GetAnswer(prompt="What is the meaning of life?", messages=self.messages))
```
Note: the self.messages variable stores the messages for only last conversation. The max messages that can be kept is 5.

Here is how you could make a simple chatbot with ItalyGPT

```py
from models.italygpt.model import Model

italygpt = Model()

while True:
    prompt = input("Your prompt: ")
    italygpt.GetAnswer(prompt=prompt, messages=messages)
    print(italygpt.answer)
```
