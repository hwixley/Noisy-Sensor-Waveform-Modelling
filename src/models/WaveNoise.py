from pydantic import BaseModel
from src.models.Transformer import Transformer

class WaveNoise(BaseModel):
    frequency: Transformer
    amplitude: Transformer
    phase: Transformer
    offset: Transformer