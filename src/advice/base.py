from .__external__ import FunctionWrapper, FunctionCaller


class Advice:
    def get_proxy(self, function):
        runner = FunctionCaller(function, self._get_runtime)

        return FunctionWrapper(function, runner)

    def _get_runtime(self, args, kwargs):
        raise NotImplementedError
