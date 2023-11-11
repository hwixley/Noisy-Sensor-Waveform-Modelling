from src.models.SensorWave import SensorWave
from src.models.WaveNoise import WaveNoise
from src.models.Transformer import Transformer
import matplotlib.pyplot as plt
from time import sleep

class SensorWavePlotter:

    def __init__(self, sensor: SensorWave):
        self.sensor = sensor

    def plot(self, N: int):
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        plt.plot(self.sensor.get_raw_sample(1000), color=colors[0], label=f'Truth')
        for i in range(N):
            noise = WaveNoise()
            noise.phase = Transformer(offset=i+1)
            plt.plot(self.sensor.get_sample_with_noise(1000, noise=noise), color=colors[i+1], label=f'Sensor {i}')

        plt.legend()
        plt.show(block=True)