import pytest

from .aspect import Aspect
from .aspectable import Aspectable


@pytest.fixture
def instance():
    def method_advice(self, arg):
        yield

    aspect_one = Aspect.from_function_kwargs(
        method=method_advice
    )

    aspect_two = Aspect.from_function_kwargs(
        method=method_advice
    )

    class SomeClass:
        def method(self, arg):
            pass

    class SomeClassWithAspect(SomeClass, metaclass=Aspectable, aspect_set=[
        aspect_one, aspect_two
    ]):
        pass

    return SomeClassWithAspect


def test_constructor_ok(instance):
    assert isinstance(instance, Aspectable)
