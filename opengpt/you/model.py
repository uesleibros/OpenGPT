from typing import List, Optional, Dict, Union
from .tools.typing.response import ModelResponse
import sys, re
import uuid
import logging
import tls_client
import fake_useragent
import json

class Model:
	@classmethod
	def __init__(self: type) -> None:
		self.__SETUP_LOGGER()
		self.__response: Dict[str, str] = {"prompt": '', "answer": '', "externalLinks": []}
		self.__session: object = tls_client.Session(client_identifier="chrome_108")
		self.__URI: str = "https://you.com/api/streamingSearch"
		self.__USER_AGENT: str = fake_useragent.UserAgent().random
		self.__ID: str = str(uuid.uuid4())
		self.__PARAMS: Dict[str, str] = {"mkt": ''}
		self.__HEADERS: Dict[str, str] = {
			"Access-Control-Allow-Origin": "*",
			"Authority": "you.com",
			"Accept": "text/event-stream",
			"Accept-Language": "pt-BR,en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3",
			"Accept-Encoding": "gzip, deflate, br",
			"Cache-Control": "no-cache, no-transform",
			"CF-Cache-Status": "DYNAMIC",
			"Referer": "https://you.com/search?q=who+are+you&tbm=youchat&cfr=chat",
			"Sec-Ch-Ua": "\"Chromium\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
			"Sec-Ch-Ua-Mobile": "?0",
			"Sec-Ch-Ua-Plataform": "\"Windows\"",
			"Sec-Fetch-Dest": "empty",
			"Sec-Fetch-Mode": "cors",
			"Sec-Fetch-Site": "same-origin",
			"Alt-Svc": "h3=\":443\"; ma=86400, h3-29=\":443\"; ma=86400",
			"User-Agent": self.__USER_AGENT,
			"Cookie": f"safesearch_guest=Moderate; uuid_guest={self.__ID}"		
		}

	@classmethod
	def __SETUP_LOGGER(self: type) -> None:
		self.__logger: logging.getLogger = logging.getLogger(__name__)
		self.__logger.setLevel(logging.DEBUG)
		console_handler: logging.StreamHandler = logging.StreamHandler()
		console_handler.setLevel(logging.DEBUG)


		formatter: logging.Formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		console_handler.setFormatter(formatter)

		self.__logger.addHandler(console_handler)

	@classmethod
	def SetupConversation(self: type, prompt: str, history: Optional[List[dict]] = []) -> None:
		self.__PARAMS: Dict[str, Union[str, int, bool]] = {
			'q': prompt,
			"page": 1,
			"count": 10,
			"safeSearch": "Moderate",
			"onShoppingPage": False,
			"mkt": '',
			"responseFilter": "WebPages,Translations,TimeZone,Computation,RelatedSearches",
			"domain": "youchat",
			"queryTraceId": self.__ID,
			"chat": str(history),
			"chatId": self.__ID,
		}

		self.__response["prompt"] = prompt

	@classmethod
	def __ERROR_ON_RESPONSE(self: type) -> None:
		self.__logger.error("Unable to fetch the response, Please try again.")
		sys.exit(1)

	@classmethod
	def SendConversation(self: type) -> ModelResponse:
		self.__session.headers = self.__HEADERS

		output: object = self.__session.get(self.__URI, params=self.__PARAMS)

		if "youChatToken" not in output.text:
			self.__ERROR_ON_RESPONSE()

		idx: int = 0
		events: List[str] = output.text.split('\n')

		text: str= ''
		externalLinks: List[Dict[str, str]] = json.loads(re.search(
			r"(?<=event: thirdPartySearchResults\ndata:)(.*\n)*?(?=event: )", output.text
			).group())["search"]["third_party_search_results"]

		while events[idx].strip() != "event: done":
		   if events[idx].strip() == "event: youChatToken":
		       idx += 1
		       if events[idx].startswith("data:"):
		           text += json.loads(events[idx].replace("data:", '').strip())["youChatToken"]
		   idx += 1

		self.__response["answer"] = text
		self.__response["externalLinks"] = externalLinks
		
		return ModelResponse(**self.__response)
