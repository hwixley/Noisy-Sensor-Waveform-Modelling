from src.SensorWavePlotter import SensorWavePlotter
from src.models.RawWave import RawWave
from src.models.SensorWave import SensorWave
from src.models.WaveNoise import WaveNoise
from src.models.Transformer import Transformer
from src.models.Fuzz import Fuzz

if __name__ == '__main__':
    wave = RawWave(frequency=4, amplitude=1.0, phase=0.0, offset=0.0, sample_rate=100)
    noise_transformer = Transformer(coefficient=0.2, offset=1.0)
    noise = WaveNoise(phase=noise_transformer, offset=Transformer(fuzz=Fuzz(coefficient=0.1, offset=0.1)))
    plotter = SensorWavePlotter(SensorWave(wave=wave, noise=noise))
    plotter.plot(3,150)