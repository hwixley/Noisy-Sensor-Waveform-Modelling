from src.models.Transformer import Transformer
from src.models.Fuzz import Fuzz
from src.models.WaveNoise import WaveNoise

wave_noise1 = WaveNoise(
    frequency=Transformer(
        coefficient=1.0,
        offset=0.0,
        fuzz=Fuzz(
            coefficient=0.0,
            offset=0.0
        )
    ),
    amplitude=Transformer(
        coefficient=1.0,
        offset=0.0,
        fuzz=Fuzz(
            coefficient=0.0,
            offset=0.0
        )
    ),
    phase=Transformer(
        coefficient=1.0,
        offset=1.0,
        fuzz=Fuzz(
            coefficient=0.0,
            offset=0.1
        )
    ),
    offset=Transformer(
        coefficient=1.0,
        offset=0.0,
        fuzz=Fuzz(
            coefficient=0.0,
            offset=0.0
        )
    )
)