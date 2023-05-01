from models.forefront.model import Model
from models.forefront.tools.system.email_creation import Email

email = Email()
res = email.CreateAccount()

client = res.client
sessionID = res.sessionID

forefront = Model(sessionID=sessionID, client=client, model="gpt-3.5-turbo")
forefront.SetupConversation("Create a story where the child can get rich in less than 3 days.")

for r in forefront.SendConversation():
	print(r.choices[0].delta.content, end='')
