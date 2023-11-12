from src.SensorWavePlotter import SensorWavePlotter
from src.models.SensorWave import SensorWave
from src.data.wave_noises import wave_noise1
from src.data.waves import wave1

if __name__ == '__main__':
    sensor1 = SensorWave(wave=wave1, noise=wave_noise1)
    sensor2 = SensorWave(wave=wave1, noise=wave_noise1)
    plotter = SensorWavePlotter(sensors=[sensor1, sensor2])

    plotter.plot(2,150)