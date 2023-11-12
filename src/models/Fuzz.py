from pydantic import BaseModel

class Fuzz(BaseModel):
    coefficient: float = 0
    offset: float = 0