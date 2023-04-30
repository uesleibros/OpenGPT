from models.you.model import Model

chat = []
youapi = Model()

youapi.SetupConversation(prompt="Hello, how are you?", history=chat)

res = youapi.SendConversation()
chat.append(res)
print("Bot: ", res.answer, end="\n\n")
