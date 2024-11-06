import pytest
from lottie.objects.properties import KeyframeBezier, Keyframe, AnimatableMixin

class TestKeyframeBezier:
    def test_from_keyframe(self):
        """Testa a criação de KeyframeBezier a partir de um Keyframe."""
        keyframe = Keyframe()
        keyframe.out_value = 1
        keyframe.in_value = 2
        obj = KeyframeBezier.from_keyframe(keyframe)
        assert obj.h1 == 1
        assert obj.h2 == 2

class TestAnimatableMixin:
    def test_clear_animation(self):
        """Testa o método clear_animation do AnimatableMixin."""
        obj = AnimatableMixin()
        obj.clear_animation(123)
        assert obj.value == 123
        assert obj.animated is False
        assert obj.keyframes is None
