import matplotlib.pyplot as plt
import numpy as np
from src.models.SensorWave import SensorWave

class SensorWavePlotter:

    sensors: [SensorWave]

    def __init__(self, sensors: [SensorWave] = []):
        self.sensors = sensors

    def plot(self, R: int, M: int = 1000):
        color = iter(plt.cm.rainbow(np.linspace(0, 1, (R+1)*len(self.sensors))))

        for i, sensor in enumerate(self.sensors):
            plt.plot(*sensor.get_raw_data(M), color=next(color), label=f'S{i+1}: f={sensor.wave.frequency}, a={sensor.wave.amplitude}, p={sensor.wave.phase}, o={sensor.wave.offset}, sr={sensor.wave.sample_rate}')
            for j in range(R):
                plt.plot(*sensor.get_noise_data(M), color=next(color), label=f'S{i+1}: #{j+1}')

        plt.title(f"Plot of True Sensor Readings vs. Noisy Ones (S={len(self.sensors)}, R={R}, M={M})")
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.grid(True)
        plt.show(block=True)