from pydantic import BaseModel
from typing import Optional, Union, Dict, List

class ExternalLinks(BaseModel):
	name: str
	url: str
	displayUrl: str
	snippet: str
	language: Optional[Union[str, None]] = ''
	thumbnailUrl: Optional[Union[str, None]] = ''
	isFamilyFriendly: Optional[Union[str, None]] = ''
	isNavigational: Optional[Union[str, None]] = ''
	snmixLink: Optional[Union[str, None]] = ''

class ModelResponse(BaseModel):
	prompt: str
	answer: Optional[str] = ''
	externalLinks: Optional[List[ExternalLinks]] = []