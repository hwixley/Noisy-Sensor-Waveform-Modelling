from pydantic import BaseModel
from typing import Optional
import numpy as np

class RawWave(BaseModel):
    frequency: float
    amplitude: float
    phase: float
    offset: float
    sample_rate: float

    def get_sample(self, N: int):
        return np.array([self.amplitude * np.sin(2 * np.pi * self.frequency * (i / self.sample_rate) + self.phase) + self.offset for i in range(N)])