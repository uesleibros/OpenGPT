from opengpt import OpenGPT

hotpot = OpenGPT(provider="hotpot", type="image", options={"style": "Portrait Anime 1"})
print(hotpot.Generate("Man with Red T-Shirt and Blue Light Hair").url)