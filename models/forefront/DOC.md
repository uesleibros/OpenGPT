# Table of Contents
- Defining Values
  - [With Account](#With-created-Account)
  - [Without Account](#Without-Account)
- Using Model
  - [Using ForeFront.AI](#Using-ForeFront.AI)

# How to Use

First you need to import the model and the system to create email, example:

```py
from models.forefront.model import Model
from models.forefront.tools.system.email_creation import Email
```

After importing let's confirm some things. Firstly, if you already have a ForeFront.ai account, you can use it as follows:

## With created Account

### Step 1

Go to the chat with AI page [`/chat`](https://chat.forefront.ai) and then open your terminal and go to the `Applications` tab.

![Applications Tab](https://cdn.discordapp.com/attachments/814722115831595018/1102442650415681546/image.png)
![Cookies Tab](https://cdn.discordapp.com/attachments/814722115831595018/1102442837649412188/image.png)

### Step 2

You will take your Customer Token and keep it.

![Client Token](https://cdn.discordapp.com/attachments/814722115831595018/1102443129140949012/image.png)

### Step 3

Now you will need to get your `session_id`. To do this you will first have to go to the `Network` tab.

![Network Tab](https://cdn.discordapp.com/attachments/814722115831595018/1102443624664399882/image.png)

If nothing appears, just reload the page with this tab open. After that, check the option to only receive requests.

![Fetch/XHR](https://cdn.discordapp.com/attachments/814722115831595018/1102443860568838185/image.png)

### Step 4

Now you will look for the request that you have written in it `touch?_clerk_js_version=4.38.4`

![touch](https://cdn.discordapp.com/attachments/814722115831595018/1102444199414075444/image.png)

Click on any of those I had and it will get your session_id.

![SessionID](https://cdn.discordapp.com/attachments/814722115831595018/1102444640608735262/image.png)

Now you can save these obtained values ​​in variables to use them later.

```py
client = "your_client"
sessionID = "your_session_id"
```

## Without Account

If you don't have an account you can simply use the function that we imported from Email.

```py
email = Email() # Intialize a class
```

Now you will use the `CreateAccount` property.

```py
res = email.CreateAccount()
```

It will take some time to create the account, but after creating it, it will return some values ​​like: `client` and `sessionID`. You can store these values in variables for later use.

```py
client = res.client
sessionID = res.sessionID
```

> **Attention:** You can create several accounts and have several of these values, so you don't need to create an account for each time you use it, just use the data from the other account created.

## Using ForeFront.AI

With the values we got we can use them easily, first we need to initialize and pass some values to the class:

```py
forefront = Model(sessionID=sessionID, client=client, model="gpt-3.5-turbo")
```

If you want to use GPT-4 you can pass the value `gpt-4` in the `model=` field.
Now to configure the conversation you can do the following:

```py
forefront.SetupConversation("Your prompt here.")
```

To get the answer you can do the following:

```py
for r in forefront.SendConversation():
	print(r.choices[0].delta.content, end='')
```

The complete code would look like this:

```py
from models.forefront.model import Model
from models.forefront.tools.system.email_creation import Email

client = "MY_CLIENT"
sessionID = "MY_SESSION"

forefront = Model(sessionID=sessionID, client=client, model="gpt-3.5-turbo")
forefront.SetupConversation("Create a story where the child can get rich in less than 3 days.")

for r in forefront.SendConversation():
	print(r.choices[0].delta.content, end='')
```