from pydantic import BaseModel
import numpy as np
from src.models.Transformer import Transformer
from typing import Optional
from src.models.Fuzz import Fuzz

frequency_fuzz=Fuzz() #0, 1e-1) #1e-2, 0.1)
amplitude_fuzz=Fuzz()#0, 0) #5e-1)
phase_fuzz=Fuzz() #1e-1, 0.0)
offset_fuzz=Fuzz()

class WaveNoise(BaseModel):
    frequency: Transformer = Transformer(fuzz=frequency_fuzz)
    amplitude: Transformer = Transformer(fuzz=amplitude_fuzz)
    phase: Transformer = Transformer(fuzz=phase_fuzz)
    offset: Transformer = Transformer(fuzz=offset_fuzz)