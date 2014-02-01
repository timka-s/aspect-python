from copy import copy


def FunctionCaller(method, handler_factory):
    def caller(*args, **kwargs):
        handler = handler_factory(args, kwargs)

        handler.before()

        try:
            result = method(*args, **kwargs)
        except BaseException as error:
            handler.throw(copy(error))

            raise error
        else:
            handler.after(result)

            return result

    return caller
