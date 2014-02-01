from copy import copy

from .__external__ import FunctionWrapper


class Advice:
    def get_using_problems(self, method):
        return []

    def get_proxy(self, function):
        runner = self._get_runner(function)

        return FunctionWrapper(function, runner)

    def _get_runner(self, function):
        runtime_factory = self._get_runtime

        def runner(*args, **kwargs):
            runtime = runtime_factory(args, kwargs)

            runtime.before()

            try:
                result = function(*args, **kwargs)
            except BaseException as error:
                # Copy to prevent changes in error.traceback
                runtime.throw(copy(error))

                raise error
            else:
                runtime.after(result)

                return result

        return runner

    def _get_runtime(self, args, kwargs):
        raise NotImplementedError
