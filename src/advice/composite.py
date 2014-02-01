from itertools import chain

from .base import Advice
from .composite_runtime import CompositeAdviceRuntime


class CompositeAdvice(Advice):
    def __init__(self, advice_set):
        self._advice_set = advice_set

    @classmethod
    def from_advice_set(cls, advice_set):
        if len(advice_set) == 1:
            return advice_set[0]

        result_advice_set = tuple(chain.from_iterable(
            advice._advice_set if isinstance(advice, cls) else [advice]
            for advice in advice_set
        ))

        return cls(result_advice_set)

    def _get_runtime(self, args, kwargs):
        return CompositeAdviceRuntime(tuple(
            advice._get_runtime(args, kwargs)
            for advice in self._advice_set
        ))
