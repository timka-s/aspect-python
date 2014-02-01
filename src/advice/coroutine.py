from .__external__ import Signature
from .base import Advice
from .coroutine_runtime import CoroutineAdviceRuntime


class CoroutineAdvice(Advice):
    def __init__(self, function, signature):
        self._function = function
        self._signature = signature

    @classmethod
    def from_function(cls, function):
        signature = Signature.from_function(function)

        return cls(function, signature)

    def get_using_problems(self, function):
        problems = []

        signature = Signature.from_function(function)

        if signature != self._signature:
            problem = 'bad_signature', function, self
            problems.append(problem)

        return problems

    def _get_runtime(self, args, kwargs):
        return CoroutineAdviceRuntime(
            self._function(*args, **kwargs)
        )
