import unittest
from lottie.parsers.sif import builder
from lottie import objects

class TestSifBuilder(unittest.TestCase):

    def setUp(self):
        self.animation = objects.Animation()

    def test_non_empty(self):
        """Test if to_sif correctly converts a non-empty Animation."""
        self.animation.width = 123
        self.animation.height = 456
        self.animation.frame_rate = 69
        self.animation.in_point = 3
        self.animation.out_point = 7
        self.animation.name = "test"

        # Add a layer to the animation
        layer = objects.layers.ShapeLayer()
        self.animation.add_layer(layer)

        sif = builder.to_sif(self.animation)
        self.assertEqual(len(sif.layers), 1)

    def test_empty_layers(self):
        """Test if to_sif correctly converts an empty Animation with layers."""
        layer = objects.layers.ShapeLayer()
        self.animation.add_layer(layer)

        sif = builder.to_sif(self.animation)
        self.assertEqual(len(sif.layers), len(self.animation.layers))

if __name__ == '__main__':
    unittest.main()
