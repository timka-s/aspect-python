from .advice import CoroutineAdvice, CompositeAdvice


class Aspect:
    def __init__(self, advice_map):
        self.advice_map = advice_map

    @classmethod
    def from_function_kwargs(cls, **function_kwargs):
        return cls({
            method_name: cls._make_advice(function_or_set)
            for method_name, function_or_set in function_kwargs.items()
        })

    @staticmethod
    def _make_advice(function_or_set):
        if isinstance(function_or_set, (list, tuple)):
            return CompositeAdvice.from_advice_set([
                CoroutineAdvice(function)
                for function in function_or_set
            ])

        return CoroutineAdvice(function_or_set)
