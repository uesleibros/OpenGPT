# How to Use

To use this model is very simple, first you need to import it:

```py
from models.cocalc.model import Model
```

After importing, we initialize the class to work with it.

```py
cocalc = Model()
```

> **Attention:** If you want more complex answers, pass the `complex` parameter as true when initializing the `Model` class.

Now we define in the `SetupConversation` function what we want to ask.

```py
cocalc.SetupConversation("prompt here")
```

Now we just run the `SendConversation` function to get the answer.

```py
print(cocalc.SendConversation().output)
```

The complete code would be like this:

```py
from models.cocalc.model import Model

cocalc = Model(complex=True)
cocalc.SetupConversation("Create an list with all popular cities of United States.")

print(cocalc.SendConversation().output)
```
