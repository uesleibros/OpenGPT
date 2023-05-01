from .tools.typing.response import ForeFrontResponse
from typing import Optional, Union, Generator, Dict, List
import fake_useragent
import tls_client
import requests
import uuid
import json
import logging

class Model:
	def __init__(self: object, sessionID: str, client: str, model: Optional[str] = "gpt-3.5-turbo", 
		persona: Optional[str] = "607e41fe-95be-497e-8e97-010a59b2e2c0", id: Optional[Union[str, None]] = None
	) -> None:
		self.__SETUP_LOGGER()
		self.__session: requests.Session = requests.Session()
		self.__model: str = model
		self.__SESSION_ID: str = sessionID
		self.__CLIENT: str = client
		self.__PERSONA: str = persona
		self.__ID: Union[str, None] = id
		self.__JSON: Dict[str, str] = {}
		self.__HEADERS: Dict[str, str] = {
			"Authority": "streaming.tenant-forefront-default.knative.chi.coreweave.com",
			"Accept": "*/*",
			"Accept-Language": "en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3",
			"Authorization": f"Bearer {self.__CLIENT}",
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

	@classmethod
	def __SETUP_LOGGER(self: type) -> None:
		self.__logger: logging.getLogger = logging.getLogger(__name__)
		self.__logger.setLevel(logging.DEBUG)
		console_handler: logging.StreamHandler = logging.StreamHandler()
		console_handler.setLevel(logging.DEBUG)
		formatter: logging.Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		console_handler.setFormatter(formatter)

		self.__logger.addHandler(console_handler)

	def SetupConversation(self: object, prompt: str) -> None:
		self.__JSON = {
			"text": prompt,
			"action": "new",
			"parentId": self.__ID,
			"workspaceId": self.__ID,
			"messagePersona": self.__PERSONA,
			"model": self.__model
		}

	def IsAccountActive(self: type) -> bool:
		__HEADERS: Dict[str, str] = {
			"Authority": "clerk.forefront.ai",
			"Accept": "*/*",
			"Cache-Control": "no-cache",
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://chat.forefront.ai",
			"Pragma": "no-cache",
			"Cookie": f"__client={self.__CLIENT}",
			"Sec-Ch-Ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
			"Sec-Ch-Ua-mobile": "?0",
			"Sec-Ch-Ua-platform": "\"macOS\"",
			"Referer": "https://chat.forefront.ai/",
			"Sec-Fetch-Dest": "empty",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Site": "same-site",
			"User-Agent": fake_useragent.UserAgent().random
		}

		return self.__session.post(f"https://clerk.forefront.ai/v1/client/sessions/{self.__SESSION_ID}/touch?_clerk_js_version=4.38.4", 
			headers=__HEADERS).status_code == 200

	def SendConversation(self: object) -> Generator[ForeFrontResponse, None, None]:
		token: str = ''
		__HEADERS: Dict[str, str] = {
			"Authority": "clerk.forefront.ai",
			"Accept": "*/*",
			"Cache-Control": "no-cache",
			"Content-Type": "application/x-www-form-urlencoded",
			"Origin": "https://chat.forefront.ai",
			"Pragma": "no-cache",
			"Cookie": f"__client={self.__CLIENT}",
			"Sec-Ch-Ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
			"Sec-Ch-Ua-mobile": "?0",
			"Sec-Ch-Ua-platform": "\"macOS\"",
			"Referer": "https://chat.forefront.ai/",
			"Sec-Fetch-Dest": "empty",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Site": "same-site",
			"User-Agent": fake_useragent.UserAgent().random
		}

		jwt_token: Dict[str, str] = self.__session.post(f"https://clerk.forefront.ai/v1/client/sessions/{self.__SESSION_ID}/tokens?_clerk_js_version=4.38.4", 
			headers=__HEADERS).json()["jwt"]

		self.__HEADERS["Authorization"] = f"Bearer {jwt_token}"
		for chunk in self.__session.post("https://streaming.tenant-forefront-default.knative.chi.coreweave.com/chat", 
			headers=self.__HEADERS, json=self.__JSON, stream=True
		).iter_lines():
			if b"finish_reason\":null" in chunk:
				data = json.loads(chunk.decode('utf-8').split("data: ")[1])

				yield ForeFrontResponse(**data)