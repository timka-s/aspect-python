import pytest

from .coroutine_runtime import CoroutineAdviceRuntime
from .coroutine import CoroutineAdvice


@pytest.fixture
def instance():
    def function(some_arg):
        pass

    return CoroutineAdvice.from_function(function)


def test_constructor_ok(instance):
    assert isinstance(instance, CoroutineAdvice)


def test_get_using_problems_ok_right_signature(instance):
    def function(some_arg):
        pass

    using_problems = instance.get_using_problems(function)

    assert set(using_problems) == set()


def test_get_using_problems_ok_bad_signature(instance):
    def function():
        pass

    using_problems = instance.get_using_problems(function)

    assert set(using_problems) == {
        ('bad_signature', function, instance)
    }


def test_get_runtime_ok(instance):
    runtime = instance._get_runtime([1], {})

    assert isinstance(runtime, CoroutineAdviceRuntime)
