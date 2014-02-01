from .base import Advice
from .coroutine_runtime import CoroutineAdviceRuntime


class CoroutineAdvice(Advice):
    def __init__(self, function):
        self._function = function

    def _get_runtime(self, args, kwargs):
        return CoroutineAdviceRuntime(
            self._function(*args, **kwargs)
        )
