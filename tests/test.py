from opengpt import OpenGPT

hotpot = OpenGPT(provider="hotpot", type="image", options={"style": "Acrylic Art"})
print(hotpot.Generate("Man with Black T-Shirt").url)