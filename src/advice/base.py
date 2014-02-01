from .__external__ import FunctionWrapper


class Advice:
    def get_proxy(self, function):
        return FunctionWrapper(function, self._get_runtime)

    def _get_runtime(self, args, kwargs):
        raise NotImplementedError
