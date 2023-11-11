from pydantic import BaseModel
from src.models.RawWave import RawWave
from src.models.WaveNoise import WaveNoise
import numpy as np

class SensorWave(BaseModel):
    wave: RawWave
    noise: WaveNoise

    def get_raw_sample(self, N: int):
        return self.wave.get_sample(N)

    def get_sample_with_noise(self, N: int, noise: WaveNoise = None):
        samples = []
        if noise is None:
            noise = self.noise

        for i in range(N):
            samples.append(noise.amplitude.transform(self.wave.amplitude) * np.sin(2 * np.pi * noise.frequency.transform(self.wave.frequency) * (i / self.wave.sample_rate) + noise.phase.transform(self.wave.phase)) + noise.offset.transform(self.wave.offset))

        return np.array(samples)