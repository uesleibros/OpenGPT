from unfinished.forefront.model import Model
from unfinished.forefront.tools.system.email_creation import Email

email = Email()
val = email.CreateAccount() # Create account to use

token = val.token
session_id = val.sessionID

forefront = Model(token=token, session_id=session_id, model="gpt-4")
forefront.SetupConversation("Better Minecraft soundtrack's")

print(forefront.SendConversation())
