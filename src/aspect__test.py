import pytest

from .advice import CoroutineAdvice
from .aspect import Aspect


@pytest.fixture
def instance():
    def some_function(*args):
        pass

    return Aspect.from_function_kwargs(
        some_method=some_function,
        other_method=some_function
    )


def test_constructor_ok(instance):
    assert isinstance(instance, Aspect)

    for advice in instance.advice_map.values():
        assert isinstance(advice, CoroutineAdvice)
