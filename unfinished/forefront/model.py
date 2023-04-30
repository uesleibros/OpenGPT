from .tools.system.email_creation import Email
from typing import Optional, Union, Generator, Dict
from browser_cookie3 import chrome
import fake_useragent
import tls_client
import requests
import uuid
import json

class Model:
	def __init__(self: object, token: str, session_id: str, model: Optional[str] = "gpt-3.5-turbo", id: Optional[Union[str, None]] = None) -> None:
		self.__session: requests.Session = requests.Session()
		self.__model: str = model
		self.__token: str = token
		self.__sessionID: str = session_id
		self.__PERSONA: str = "607e41fe-95be-497e-8e97-010a59b2e2c0"
		self.__ID: Union[str, None] = id
		self.__JSON: Dict[str, str] = {}
		self.__HEADERS: Dict[str, str] = {
			"Authority": "chat-server.tenant-forefront-default.knative.chi.coreweave.com",
			"Accept": "*/*",
			"Accept-Language": "en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3",
			"Authorization": "Bearer " + self.__token,
			"Cache-Control": "no-cache",
			"Content-Type": "application/json",
			"Origin": "https://chat.forefront.ai",
			"Pragma": "no-cache",
			"Referer": "https://chat.forefront.ai/",
			"Sec-Ch-Ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
			"Sec-Ch-Ua-mobile": "?0",
			"Sec-Ch-Ua-platform": "\"macOS\"",
			"Sec-Fetch-Dest": "empty",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Site": "cross-site",
			"User-Agent": fake_useragent.UserAgent().random
		}

		if self.__ID is None:
			self.__ID = str(uuid.uuid4())

	def SetupConversation(self: object, prompt: str) -> None:
		self.__JSON = {
			"text": prompt,
			"action": "new",
			"parentId": self.__ID,
			"workspaceId": self.__ID,
			"messagePersona": self.__PERSONA,
			"model": self.__model
		}

	def SendConversation(self: object):
		token: str = ''
		for chunk in requests.post("https://chat-server.tenant-forefront-default.knative.chi.coreweave.com/chat", 
			headers=self.__HEADERS, json=self.__JSON, stream=True
		).iter_lines():
			if b"finish_reason\":null" in chunk:
				data = json.loads(chunk.decode('utf-8').split("data: ")[1])

				if "content" in data["choices"][0]["delta"]:
					token += data["choices"][0]["delta"].get("content")
		return token
