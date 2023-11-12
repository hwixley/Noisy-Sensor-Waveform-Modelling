from pydantic import BaseModel
import numpy as np
from src.models.Fuzz import Fuzz
from typing import List

class Transformer(BaseModel):

    coefficient: float = 1.0
    offset: float = 0.0
    fuzz: Fuzz = Fuzz()
    

    def transform(self, samples: List[float] or float) -> List[float] or float:
        if isinstance(samples, float):
            return samples*self.coeff() + self.off()
        else:
            return np.array(samples)*self.coeff() + self.off()
    
    def coeff(self):
        return self.coefficient*np.random.normal(scale=self.fuzz.coefficient)
    
    def off(self):
        return self.offset + np.random.normal(scale=self.fuzz.offset)