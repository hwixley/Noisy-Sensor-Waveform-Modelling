from src.SensorWavePlotter import SensorWavePlotter
from src.models.RawWave import RawWave
from src.models.SensorWave import SensorWave
from src.models.WaveNoise import WaveNoise
from src.models.Transformer import Transformer

if __name__ == '__main__':
    wave = RawWave(frequency=4, amplitude=1.0, phase=0.0, offset=0.0, sample_rate=1000)
    noise_transformer = Transformer(coefficient=0.3, offset=1.0)
    noise = WaveNoise(phase=noise_transformer)
    plotter = SensorWavePlotter(SensorWave(wave=wave, noise=noise))
    plotter.plot(3)