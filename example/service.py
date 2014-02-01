data_proxy = {
    'key': 'value',
    'sub_key': 'sub_value'
}.__getitem__


class ServiceError(Exception):
    pass


class Service:
    _lookup_map = {}

    def __init__(self, name):
        self._fill(name)

    def _fill(self, name):
        self._lookup_map[name] = self

        self._name = name

    def do_some_work(self, argument):
        try:
            return data_proxy(argument)
        except:
            raise ServiceError
