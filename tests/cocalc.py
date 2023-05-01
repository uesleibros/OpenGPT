from models.cocalc.model import Model

cocalc = Model(complex=True)
cocalc.SetupConversation("Create an list with all popular cities of United States.")

print(cocalc.SendConversation().output)