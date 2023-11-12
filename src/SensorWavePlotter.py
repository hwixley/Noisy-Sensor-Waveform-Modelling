import matplotlib.pyplot as plt
from typing import Optional
import numpy as np
from src.models.RawWave import RawWave
from src.models.WaveNoise import WaveNoise
from src.models.SensorWave import SensorWave

class SensorWavePlotter:

    sensor: SensorWave

    def __init__(self, sensor: Optional[SensorWave] = None, sensor_wave: Optional[RawWave] = None, sensor_noise: Optional[WaveNoise] = None):
        self.sensor = sensor or SensorWave(wave=sensor_wave, noise=sensor_noise)

    def plot(self, N: int, M: int = 1000):
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        plt.plot(*self.sensor.get_raw_data(M), color=colors[0], label=f'Truth')
        for i in range(N):
            plt.plot(*self.sensor.get_noise_data(M), color=colors[i+1], label=f'Sensor {i}')

        plt.legend()
        plt.show(block=True)