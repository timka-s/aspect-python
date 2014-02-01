from .function_wrapper import FunctionWrapper


def test_ok():
    def function(
            arg, arg_with_default='arg_with_default', *,
            kw, kw_with_default='kw_with_default'):
        return arg, arg_with_default, kw, kw_with_default

    instance = FunctionWrapper(function, function)

    expected_result = ('arg', 'arg_with_default', 'kw', 'kw_with_default')
    captured_result = instance(expected_result[0], kw=expected_result[2])

    assert captured_result == expected_result
