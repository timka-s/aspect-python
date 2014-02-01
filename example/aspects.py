from src import make_aspect
from .service import Service


def check_replace(self: Service, name):
    if name in self._lookup_map:
        print('Will be replaced service instance', name)

    yield


def control_creation(self: Service, name):
    print('Started creation of service', name)

    yield

    print('Finished creation of service', name)


def control_working(self: Service, argument):
    try:
        result = yield
    except:
        print('Exception for argument', argument)
    else:
        print('Result for argument ', argument, result)


life_aspect = make_aspect(
    _fill=[check_replace, control_creation],
    do_some_work=control_working
)


def deprecation_aspect_factory(deprecated_argument_set):
    def check_deprecated_argument(self: Service, argument):
        if argument in deprecated_argument_set:
            print('Deprecated argument', argument)

        yield

    return make_aspect(
        do_some_work=check_deprecated_argument
    )
