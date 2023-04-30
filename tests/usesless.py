from models.usesless.model import Model

usesless = Model(model="gpt-4")

while True:
	prompt = input("You: ")
	usesless.SetupConversation(prompt=prompt)

	print("\n\nBot: ", end='')
	for resp in usesless.SendConversation():
		print(resp.choices[0].delta.content, end='')
	print("\n\n")
