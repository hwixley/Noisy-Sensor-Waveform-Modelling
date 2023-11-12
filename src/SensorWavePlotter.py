import matplotlib.pyplot as plt
import numpy as np
from src.models.SensorWave import SensorWave

class SensorWavePlotter:

    sensors: [SensorWave]

    def __init__(self, sensors: [SensorWave] = []):
        self.sensors = sensors

    def plot(self, N: int, M: int = 1000):
        color = iter(plt.cm.rainbow(np.linspace(0, 1, (N+1)*len(self.sensors))))

        for i, sensor in enumerate(self.sensors):
            plt.plot(*sensor.get_raw_data(M), color=next(color), label=f'S{i+1}: f={sensor.wave.frequency}, a={sensor.wave.amplitude}, p={sensor.wave.phase}, o={sensor.wave.offset}')
            for j in range(N):
                plt.plot(*sensor.get_noise_data(M), color=next(color), label=f'S{i+1}: #{j+1}')

        plt.legend()
        plt.grid(True)
        plt.show(block=True)