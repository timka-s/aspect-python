from functools import update_wrapper, WRAPPER_ASSIGNMENTS

from .__external__ import Signature
from .caller import FunctionCaller


WRAPPER_ASSIGNMENTS = WRAPPER_ASSIGNMENTS + ('__defaults__', '__kwdefaults__')

decorator_tpl = '''
def decorator(__caller):
    def wrapper({method_signature}):
        return __caller({method_call})

    return wrapper
'''


def FunctionWrapper(function, handler_factory):
    caller = FunctionCaller(function, handler_factory)

    method_signature = Signature.from_function(function)

    exec_code = decorator_tpl.format(
        method_signature=method_signature.get_signature_str(),
        method_call=method_signature.get_call_str(),
    )
    exec_ns = {}

    exec(exec_code, exec_ns)

    wrapper = exec_ns['decorator'](caller)

    return update_wrapper(wrapper, function, assigned=WRAPPER_ASSIGNMENTS)
