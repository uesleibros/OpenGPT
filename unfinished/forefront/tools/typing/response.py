from pydantic import BaseModel

class EmailResponse(BaseModel):
	token: str
	sessionID: str