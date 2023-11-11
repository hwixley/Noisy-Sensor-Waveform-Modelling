from pydantic import BaseModel

class Fuzz(BaseModel):

    coefficient: float = 0
    offset: float = 0

    def __init__(self, coefficient: float = 0.0, offset: float = 0.0):
        super().__init__()
        self.coefficient = coefficient
        self.offset = offset