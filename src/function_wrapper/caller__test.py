import pytest

from .caller import FunctionCaller


def function(*, result, error, raise_error):
    if raise_error:
        raise error()
    else:
        return result


class HandlerFactory:
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


@pytest.fixture
def instance():
    return FunctionCaller(function, HandlerFactory)


@pytest.mark.parametrize('raise_error', [False, True])
def test_ok(instance, raise_error):
    error = IOError

    try:
        instance(result='result', error=error, raise_error=raise_error)
    except error:
        pass