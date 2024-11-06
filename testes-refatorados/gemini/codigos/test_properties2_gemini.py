import pytest
from lottie.objects.properties import KeyframeBezier, Keyframe, OffsetKeyframe, AnimatableMixin


def test_keyframe_bezier_from_keyframe_copies_values():
    """
    Test that KeyframeBezier.from_keyframe correctly copies in and out values.
    """
    keyframe = Keyframe()
    keyframe.out_value = 1
    keyframe.in_value = 2

    obj = KeyframeBezier.from_keyframe(keyframe)

    assert obj.h1 == keyframe.out_value  # Use 'out_value' for consistency
    assert obj.h2 == keyframe.in_value   # Use 'in_value' for consistency


def test_animatable_mixin_clear_animation():
    """
    Test that AnimatableMixin.clear_animation resets properties correctly.
    """
    obj = AnimatableMixin()
    obj.value = 123
    obj.animated = True
    obj.keyframes = [Keyframe()]  # Set a dummy keyframe

    obj.clear_animation()

    assert obj.value == 123
    assert not obj.animated
    assert obj.keyframes is None