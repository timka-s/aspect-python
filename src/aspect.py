from .advice import CoroutineAdvice


class Aspect:
    def __init__(self, advice_map):
        self.advice_map = advice_map

    @classmethod
    def from_function_kwargs(cls, **function_kwargs):
        return cls({
            method_name: CoroutineAdvice(function)
            for method_name, function in function_kwargs.items()
        })
