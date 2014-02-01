import pytest

from .base import Advice


@pytest.fixture
def instance():
    return Advice()


def test_get_using_problems_ok(instance):
    assert instance.get_using_problems(lambda x: x) == []


def test_get_proxy_ok(instance):
    def _get_runtime(args, kwargs):
        pass

    instance._get_runtime = _get_runtime

    assert instance.get_proxy(lambda x: x)


def test_get_runtime_error_not_implemented(instance):
    with pytest.raises(NotImplementedError):
        instance._get_runtime([], {})


@pytest.mark.parametrize('raise_error', [False, True])
def test_get_runner_ok(instance, raise_error):
    class Runtime:
        def __init__(self, args, kwargs):
            self.expected_result = kwargs['result']
            self.expected_error = kwargs['error']

            self.state = 'init'

        def before(self):
            assert self.state == 'init'

            self.state = 'before'

        def after(self, result):
            assert self.state == 'before'
            assert self.expected_result == result

            self.state = 'after'

        def throw(self, error):
            assert self.state == 'before'
            assert isinstance(error, self.expected_error)

            self.state = 'throw'

    instance._get_runtime = Runtime

    def function(*, result, error, raise_error):
        if raise_error:
            raise error()
        else:
            return result

    runner = instance._get_runner(function)

    error = IOError

    try:
        runner(result='result', error=error, raise_error=raise_error)
    except error:
        pass
