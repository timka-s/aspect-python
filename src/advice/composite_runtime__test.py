import pytest

from .base_runtime import AdviceRuntime
from .composite_runtime import CompositeAdviceRuntime


class SomeAdviceRuntime(AdviceRuntime):
    def before(self):
        self.check_before = True

    def after(self, result):
        self.check_after = result

    def throw(self, error):
        self.check_throw = error


@pytest.fixture
def instance():
    return CompositeAdviceRuntime([
        SomeAdviceRuntime(),
        SomeAdviceRuntime()
    ])


def test_before_ok(instance):
    for runtime in instance._runtime_set:
        assert not hasattr(runtime, 'check_before')

    instance.before()

    for runtime in instance._runtime_set:
        assert runtime.check_before


def test_after_ok(instance):
    for runtime in instance._runtime_set:
        assert not hasattr(runtime, 'check_after')

    result = object()

    instance.after(result)

    for runtime in instance._runtime_set:
        assert runtime.check_after is result


def test_throw_ok(instance):
    for runtime in instance._runtime_set:
        assert not hasattr(runtime, 'check_throw')

    error = Exception()

    instance.throw(error)

    for runtime in instance._runtime_set:
        assert runtime.check_throw is error
