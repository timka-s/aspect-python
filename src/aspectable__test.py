import pytest

from .aspect import Aspect
from .aspectable import Aspectable


@pytest.fixture
def instance():
    def method_advice(self, arg):
        yield

    aspect = Aspect.from_function_kwargs(
        method=method_advice
    )

    class SomeClass:
        def method(self, arg):
            pass

    class SomeClassWithAspect(SomeClass, metaclass=Aspectable, aspect=aspect):
        pass

    return SomeClassWithAspect


def test_constructor_ok(instance):
    assert isinstance(instance, Aspectable)
