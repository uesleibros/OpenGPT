from typing import Dict, Optional, Generator
from .tools.typing.response import CoCalcResponse
import requests
import uuid
import fake_useragent

class Model:
   @classmethod
   def __init__(self: type, complex: Optional[bool] = False) -> None:
      self.__session: requests.Session = requests.Session()
      self.__SYSTEM: str = "ASSUME I HAVE FULL ACCESS TO COCALC. ENCLOSE MATH IN $."
      if complex:
         self.__SYSTEM += "INCLUDE THE LANGUAGE DIRECTLY AFTER THE TRIPLE BACKTICKS IN ALL MARKDOWN CODE BLOCKS. How can I do the following using CoCalc?"
      self.__ID: uuid.uuid4 = uuid.uuid4()
      self.__JSON: Dict[str, str] = {
         "input": '',
         "system": self.__SYSTEM,
         "tag": "next:index"
      }
      self.__HEADERS: Dict[str, str] = {
         "Authority": "cocalc.com",
         "Accept": "*/*",
         "Accept-Language": "pt-BR,en;q=0.9,en-US;q=0.8,en;q=0.7",
         "Cookie": f"CC_ANA={self.__ID};",
         "Origin": "https://cocalc.com",
         "Referer": "https://cocalc.com/",
         "Sec-Ch-Ua": "\"Not:A-Brand\";v=\"99\", \"Chromium\";v=\"112\"",
         "User-Agent": fake_useragent.UserAgent().random
      }

   @classmethod
   def SetupConversation(self: type, prompt: str) -> None:
      self.__JSON["input"] = prompt

   @classmethod
   def SendConversation(self: type) -> Generator[CoCalcResponse, None, None]:
      data = self.__session.post("https://cocalc.com/api/v2/openai/chatgpt", headers=self.__HEADERS, json=self.__JSON)
      
      return CoCalcResponse(**data.json())