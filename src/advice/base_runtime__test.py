import pytest

from .base_runtime import AdviceRuntime


@pytest.fixture
def instance():
    return AdviceRuntime()


def test_before_error_not_implemented(instance):
    with pytest.raises(NotImplementedError):
        instance.before()


def test_after_error_not_implemented(instance):
    with pytest.raises(NotImplementedError):
        instance.after(object())


def test_throw_error_not_implemented(instance):
    with pytest.raises(NotImplementedError):
        instance.throw(Exception())
