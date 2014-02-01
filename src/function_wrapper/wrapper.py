from functools import update_wrapper, WRAPPER_ASSIGNMENTS

from .__external__ import Signature


WRAPPER_ASSIGNMENTS = WRAPPER_ASSIGNMENTS + ('__defaults__', '__kwdefaults__')

decorator_tpl = '''
def decorator(__function__):
    def wrapper({function_signature}):
        return __function__({function_call})

    return wrapper
'''


def FunctionWrapper(source_function, target_function):
    function_signature = Signature.from_function(source_function)

    exec_code = decorator_tpl.format(
        function_signature=function_signature.get_signature_str(),
        function_call=function_signature.get_call_str(),
    )
    exec_ns = {}

    exec(exec_code, exec_ns)

    wrapper = exec_ns['decorator'](target_function)

    return update_wrapper(
        wrapper,
        source_function,
        assigned=WRAPPER_ASSIGNMENTS
    )
