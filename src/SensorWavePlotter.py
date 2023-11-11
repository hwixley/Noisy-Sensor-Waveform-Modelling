from src.models.SensorWave import SensorWave
from src.models.WaveNoise import WaveNoise
from src.models.Transformer import Transformer
import matplotlib.pyplot as plt

class SensorWavePlotter:

    def __init__(self, sensor: SensorWave):
        self.sensor = sensor

    def plot(self, N: int, M: int = 1000):
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
        plt.plot(self.sensor.get_raw_sample(M), color=colors[0], label=f'Truth')
        for i in range(N):
            plt.plot(self.sensor.get_sample_with_noise(M), color=colors[i+1], label=f'Sensor {i}')

        plt.legend()
        plt.show(block=True)