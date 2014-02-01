import pytest

from .common import AdviceRuntimeError
from .coroutine_runtime import CoroutineAdviceRuntime


def advice(behavior=None):
    if behavior == 'before-error':
        raise Exception

    if behavior == 'throw-not-except':
        yield
    else:
        try:
            yield
        except Exception as error:
            if behavior == 'throw-re-raise':
                raise error

            if behavior == 'throw-error':
                raise Exception
        else:
            if behavior == 'after-error':
                raise Exception

    if behavior == 'not-stop':
        yield


@pytest.mark.parametrize('behavior', ['ok'])
def test_before_ok(behavior):
    instance = CoroutineAdviceRuntime(advice(behavior))

    assert instance.before() is None


@pytest.mark.parametrize('behavior', ['before-error'])
def test_before_error(behavior):
    instance = CoroutineAdviceRuntime(advice(behavior))

    with pytest.raises(AdviceRuntimeError):
        instance.before()


@pytest.mark.parametrize('behavior', ['ok'])
def test_after_ok(behavior):
    instance = CoroutineAdviceRuntime(advice(behavior))

    assert instance.before() is None
    assert instance.after({}) is None


@pytest.mark.parametrize('behavior', ['after-error', 'not-stop'])
def test_after_error(behavior):
    instance = CoroutineAdviceRuntime(advice(behavior))

    assert instance.before() is None
    with pytest.raises(AdviceRuntimeError):
        instance.after({})


@pytest.mark.parametrize('behavior', [
    'ok', 'throw-not-except', 'throw-re-raise'])
def test_throw_ok(behavior):
    instance = CoroutineAdviceRuntime(advice(behavior))

    assert instance.before() is None
    assert instance.throw(Exception()) is None


@pytest.mark.parametrize('behavior', ['throw-error', 'not-stop'])
def test_throw_error(behavior):
    instance = CoroutineAdviceRuntime(advice(behavior))

    assert instance.before() is None
    with pytest.raises(AdviceRuntimeError):
        instance.throw(Exception())
