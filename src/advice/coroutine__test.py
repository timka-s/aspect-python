import pytest

from .coroutine_runtime import CoroutineAdviceRuntime
from .coroutine import CoroutineAdvice


@pytest.fixture
def instance():
    def function(some_arg):
        pass

    return CoroutineAdvice(function)


def test_constructor_ok(instance):
    assert isinstance(instance, CoroutineAdvice)


def test_get_runtime_ok(instance):
    runtime = instance._get_runtime([1], {})

    assert isinstance(runtime, CoroutineAdviceRuntime)
