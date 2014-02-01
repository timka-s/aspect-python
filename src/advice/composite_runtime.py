from .base_runtime import AdviceRuntime


class CompositeAdviceRuntime(AdviceRuntime):
    def __init__(self, runtime_set):
        self._runtime_set = runtime_set

    def before(self):
        for runtime in self._runtime_set:
            runtime.before()

    def after(self, result):
        for runtime in self._runtime_set:
            runtime.after(result)

    def throw(self, error):
        for runtime in self._runtime_set:
            runtime.throw(error)
