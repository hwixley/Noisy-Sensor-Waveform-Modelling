from pydantic import BaseModel
from src.models.RawWave import RawWave
from src.models.WaveNoise import WaveNoise
from src.models.Transformer import Transformer
from src.models.Fuzz import Fuzz
import numpy as np
from typing import List

class SensorWave(BaseModel):
    wave: RawWave
    noise: WaveNoise

    def get_raw_data(self, N: int):
        return [self.get_labels(N), self.get_raw_sample(N)]
    
    def get_noise_data(self, N: int):
        return [self.get_labels(N), self.get_sample_with_noise(N)]
    
    # ---------------------------------------------------------------------------------------------

    def get_raw_sample(self, N: int):
        return self.wave.get_sample(N)

    def get_sample_with_noise(self, N: int, noise: WaveNoise = None):
        samples = []
        if noise is None:
            noise = self.noise

        for j in range(N):
            samples.append(self.amplitude(noise) * np.sin(2 * np.pi * self.frequency(noise) * (j / self.wave.sample_rate) + self.phase(noise)) + self.offset(noise))

        return np.array(samples)
    
    def get_labels(self, N: int):
        return np.arange(stop=N, step=1)/self.wave.sample_rate
    
    # ---------------------------------------------------------------------------------------------
    
    def amplitude(self, noise: WaveNoise = None) -> float:
        return noise.amplitude.transform(self.wave.amplitude)
    
    def frequency(self, noise: WaveNoise = None) -> List[float]:
        return noise.frequency.transform(self.wave.frequency)
    
    def phase(self, noise: WaveNoise = None) -> List[float]:
        return noise.phase.transform(self.wave.phase)
    
    def offset(self, noise: WaveNoise = None) -> List[float]:
        return noise.offset.transform(self.wave.offset)
    
    
