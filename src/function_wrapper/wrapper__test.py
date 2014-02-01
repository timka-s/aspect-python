from .wrapper import FunctionWrapper


class HandlerFactory:
    __init__ = before = after = throw = lambda *args: None


def test_ok():
    def method(
            arg, arg_with_default='arg_with_default', *,
            kw, kw_with_default='kw_with_default'):
        return arg, arg_with_default, kw, kw_with_default

    instance = FunctionWrapper(method, HandlerFactory)

    expected = ('arg', 'arg_with_default', 'kw', 'kw_with_default')
    result = instance(expected[0], kw=expected[2])

    assert expected == result
