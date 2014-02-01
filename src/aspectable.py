class Aspectable(type):
    def __new__(cls, name, bases, ns, *, aspect):
        self = type.__new__(cls, name, bases, ns)

        for method_name, advice in aspect.advice_map.items():
            method = getattr(self, method_name)
            method_proxy = advice.get_proxy(method)
            setattr(self, method_name, method_proxy)

        return self

    def __init__(self, name, bases, ns, *, aspect):
        type.__init__(self, name, bases, ns)
