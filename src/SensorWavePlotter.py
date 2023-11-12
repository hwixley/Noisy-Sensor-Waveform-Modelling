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
            plt.plot(*sensor.get_raw_data(M), color=next(color), label=f'Sensor {i} Truth')
            for j in range(N):
                plt.plot(*sensor.get_noise_data(M), color=next(color), label=f'Sensor {i} Reading {j}')

        plt.legend()
        plt.show(block=True)