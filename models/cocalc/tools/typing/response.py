from pydantic import BaseModel

class CoCalcResponse(BaseModel):
  output: str
  success: bool
