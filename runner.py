from src.SensorWavePlotter import SensorWavePlotter
from src.data.wave_noises import wave_noise1
from src.data.waves import wave1

if __name__ == '__main__':
    plotter = SensorWavePlotter(sensor_wave=wave1, sensor_noise=wave_noise1)
    plotter.plot(10,150)