from .signature import Signature


def test_from_function_ok_empty():
    def some_function():
        pass

    signature = Signature.from_function(some_function)

    assert signature.args == ()
    assert signature.varargs is None
    assert signature.kwargs == ()
    assert signature.varkwargs is None


def test_from_function_ok_complex():
    def some_function(arg1, arg2, *varargs, kw1, kw2, **varkwargs):
        pass

    signature = Signature.from_function(some_function)

    assert signature.args == ('arg1', 'arg2')
    assert signature.varargs == 'varargs'
    assert signature.kwargs == ('kw1', 'kw2')
    assert signature.varkwargs == 'varkwargs'


def test_get_signature_str_ok_kw_with_varargs():
    signature = Signature(
        ('arg1', 'arg2'), 'varargs',
        ('kw1', 'kw2'), 'varkwargs'
    )

    signature_str = signature.get_signature_str()

    assert signature_str == 'arg1, arg2, *varargs, kw1, kw2, **varkwargs'


def test_get_signature_str_ok_kw_without_varargs():
    signature = Signature(
        ('arg1', 'arg2'), None,
        ('kw1', 'kw2'), 'varkwargs'
    )

    signature_str = signature.get_signature_str()

    assert signature_str == 'arg1, arg2, *, kw1, kw2, **varkwargs'


def test_get_call_str_ok():
    signature = Signature(
        ('arg1', 'arg2'), 'varargs',
        ('kw1', 'kw2'), 'varkwargs'
    )

    call_str = signature.get_call_str()

    assert call_str == 'arg1, arg2, *varargs, kw1=kw1, kw2=kw2, **varkwargs'
