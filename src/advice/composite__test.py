import pytest

from itertools import chain

from .base import Advice
from .composite_runtime import CompositeAdviceRuntime
from .composite import CompositeAdvice


class SomeAdvice(Advice):
    def get_using_problems(self, method):
        return [
            ('test_problem', method, self)
        ]

    def _get_runtime(self, args, kwargs):
        yield


@pytest.fixture
def instance():
    return CompositeAdvice([
        SomeAdvice(),
        SomeAdvice()
    ])


def test_constructor_ok(instance):
    assert isinstance(instance, CompositeAdvice)


def test_from_advice_set_ok_one(instance):
    same_instance = CompositeAdvice.from_advice_set([instance])

    assert same_instance is instance


def test_from_advice_set_ok_two(instance):
    merge_instance = CompositeAdvice.from_advice_set([instance, instance])

    assert isinstance(merge_instance, CompositeAdvice)

    expected_advice_set = tuple(instance._advice_set + instance._advice_set)
    captured_advice_set = merge_instance._advice_set

    assert captured_advice_set == expected_advice_set


def test_get_using_problems_ok(instance):
    def function(self):
        pass

    expected_using_problems = tuple(chain.from_iterable(
        advice.get_using_problems(function)
        for advice in instance._advice_set
    ))

    captured_using_problems = instance.get_using_problems(function)

    assert captured_using_problems == expected_using_problems


def test_get_runtime_ok(instance):
    runtime = instance._get_runtime([1, 2], {})

    assert isinstance(runtime, CompositeAdviceRuntime)

