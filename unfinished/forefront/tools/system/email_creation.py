from typing import Dict, Any
from pymailtm import MailTm, Message
from ..typing.response import EmailResponse
import re
import logging
import fake_useragent
import tls_client
import string
import random
import sys
import time

class Email:
	@classmethod
	def __init__(self: type) -> None:
		self.__SETUP_LOGGER()
		self.__session: tls_client.Session = tls_client.Session(client_identifier="chrome_108")

	@classmethod
	def __SETUP_LOGGER(self: type) -> None:
		self.__logger: logging.getLogger = logging.getLogger(__name__)
		self.__logger.setLevel(logging.DEBUG)
		console_handler: logging.StreamHandler = logging.StreamHandler()
		console_handler.setLevel(logging.DEBUG)


		formatter: logging.Formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
		console_handler.setFormatter(formatter)

		self.__logger.addHandler(console_handler)

	@classmethod
	def __AccountState(self: object, output: str, field: str) -> bool:
		if field not in output:
			return False
		return True

	@classmethod
	def CreateAccount(self: object) -> str:
		mail_client: MailTm = MailTm().get_account()
		mail_address: Any = mail_client.address

		self.__session.headers = {
			"Origin": "https://accounts.forefront.ai",
			"User-Agent": fake_useragent.UserAgent().random
		}
		
		output = self.__session.post("https://clerk.forefront.ai/v1/client/sign_ups?_clerk_js_version=4.38.4", data={"email_address": mail_address}).json()

		if not self.__AccountState(str(output), "id"):
			self.__logger.error("Failed to create account :(")
			sys.exit(1)

		trace_id = output["response"]["id"]
		output = self.__session.post(f"https://clerk.forefront.ai/v1/client/sign_ups/{trace_id}/prepare_verification?_clerk_js_version=4.38.4", 
			data={"strategy": "email_link", "redirect_url": "https://accounts.forefront.ai/sign-up/verify"})

		if not self.__AccountState(output.text, "sign_up_attempt"):
			self.__logger.error("Failed to create account :(")
			sys.exit(1)

		while True:
			new_message: Message = mail_client.wait_for_message()

			verification_url = re.findall(r"https:\/\/clerk\.forefront\.ai\/v1\/verify\?token=\w.+", new_message.text)[0]
			if verification_url:
			    break

		self.__session.get(verification_url)
		output = self.__session.get("https://clerk.forefront.ai/v1/client?_clerk_js_version=4.38.4")

		token: str = output.json()["response"]["sessions"][0]["last_active_token"]["jwt"]
		sessionID: str = output.json()["response"]["sessions"][0]["id"]

		return EmailResponse(**{"token": token, "sessionID": sessionID})
