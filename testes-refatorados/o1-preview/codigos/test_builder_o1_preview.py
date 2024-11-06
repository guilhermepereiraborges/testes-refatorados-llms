import pytest
from lottie.parsers.sif import builder
from lottie import objects

class TestSifBuilder:
    def test_non_empty_animation(self):
        """Testa se to_sif converte corretamente uma Animation não vazia."""
        lot = objects.Animation(
            width=123,
            height=456,
            frame_rate=69,
            in_point=3,
            out_point=7,
            name="test"
        )

        # Adiciona uma camada à animação
        layer = objects.layers.ShapeLayer()
        lot.add_layer(layer)

        sif = builder.to_sif(lot)
        assert len(sif.layers) == 1

    def test_empty_layers(self):
        """Testa se to_sif converte corretamente uma Animation com camadas."""
        lot = objects.Animation()
        layer = objects.layers.ShapeLayer()
        lot.add_layer(layer)

        sif = builder.to_sif(lot)
        assert len(sif.layers) == len(lot.layers)
