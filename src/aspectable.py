from collections import defaultdict

from .common import AdviceApplicationError
from .advice import CompositeAdvice


class Aspectable(type):
    def __new__(cls, name, bases, ns, *, aspect_set):
        self = type.__new__(cls, name, bases, ns)

        advice_map = defaultdict(list)

        for aspect in aspect_set:
            for method_name, advice in aspect.advice_map.items():
                advice_map[method_name].append(advice)

        for method_name, advice_set in advice_map.items():
            if not hasattr(self, method_name):
                raise AdviceApplicationError(
                    'Undefined method', self, method_name
                )

            method = getattr(self, method_name)
            advice = CompositeAdvice.from_advice_set(advice_set)

            problems = advice.get_using_problems(method)
            if problems:
                raise AdviceApplicationError(
                    'Problems for method', self, method_name, method, problems
                )

            method_proxy = advice.get_proxy(method)
            setattr(self, method_name, method_proxy)

        return self

    def __init__(self, name, bases, ns, *, aspect_set):
        type.__init__(self, name, bases, ns)
