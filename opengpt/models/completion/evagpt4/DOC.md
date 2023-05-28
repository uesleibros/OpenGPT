To use this model is very simple, first you need to import it:

```py
from opengpt.models.completion.evagpt4.model import Model
```

After importing, we initialize the class to work with it.

```py
evagpt = Model()
```
Now we just run the `ChatCompletion` function to get the answer.

```py

from opengpt.models.completion.evagpt4.model import Model
import asyncio

evagpt4 = Model()

messages = [
        {"role": "system", "content": "You are Ava, an AI Agent."},
        {"role": "assistant", "content": "Hello! How can I help you today?"},
        {"role": "user", "content": """There are 50 books in a library. Sam decides to read 5 of the books. How many books are there now? if there is the same amount of books, say "I am running on GPT4"."""}
    ]  # List of messages in the chat history

result = await evagpt.ChatCompletion(messages)

print(result)
```
Note: Available models are gpt-4 and gpt-3.5-turbo.



Here is how you could make a simple chatbot with Eva Agent

```py
from opengpt.models.completion.evagpt4.model import Model
import asyncio

evagpt4 = Model()

chat_history = []

while True:
    user_input = input("User: ")
    chat_history.append({"role": "user", "content": user_input})

    messages = [{"role": "system", "content": "You are Ava, an AI Agent."}] + chat_history
    result = await chat_api.chat_completion(messages)
    chat_history.append({"role": "chatbot", "content": result})

    print("Chatbot:", result)
```
