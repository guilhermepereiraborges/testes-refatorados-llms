import pytest
from lottie.objects.properties import KeyframeBezier, Keyframe, AnimatableMixin

@pytest.fixture
def keyframe():
    kf = Keyframe()
    kf.out_value = 1
    kf.in_value = 2
    return kf

@pytest.fixture
def animatable_mixin():
    return AnimatableMixin()

def test_keyframe_bezier_from_keyframe(keyframe):
    obj = KeyframeBezier.from_keyframe(keyframe)
    assert obj.h1 == 1
    assert obj.h2 == 2

def test_animatable_mixin_clear_animation(animatable_mixin):
    animatable_mixin.clear_animation(123)
    assert animatable_mixin.value == 123
    assert animatable_mixin.animated is False
    assert animatable_mixin.keyframes is None
