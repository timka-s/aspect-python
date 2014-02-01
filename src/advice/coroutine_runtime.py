from .common import AdviceRuntimeError
from .base_runtime import AdviceRuntime


class CoroutineAdviceRuntime(AdviceRuntime):
    def __init__(self, coroutine):
        self._coroutine = coroutine

    def before(self):
        try:
            next(self._coroutine)
        except:
            raise AdviceRuntimeError('Advice raised error before yield')

    def after(self, result):
        try:
            self._coroutine.send(result)
        except StopIteration:
            pass
        except:
            raise AdviceRuntimeError('Advice raised error after yield')
        else:
            raise AdviceRuntimeError('Advice did not stop after yield')

    def throw(self, error):
        error_class = error.__class__
        error_tb = error.__traceback__

        try:
            self._coroutine.throw(error_class, error, error_tb)
        except StopIteration:
            pass
        except BaseException as advice_error:
            if error is not advice_error:
                raise AdviceRuntimeError('Advice raised own exception')
        else:
            raise AdviceRuntimeError('Advice did not stop after exception')
