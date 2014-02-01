from collections import namedtuple
from inspect import getfullargspec


SignatureTuple = namedtuple('SignatureTuple', 'args varargs kwargs varkwargs')


class Signature(SignatureTuple):
    @classmethod
    def from_function(cls, function):
        spec = getfullargspec(function)

        return cls(
            tuple(spec.args), spec.varargs,
            tuple(spec.kwonlyargs), spec.varkw
        )

    def get_signature_str(self):
        items = []

        items.extend(self.args)

        if self.varargs:
            items.append('*' + self.varargs)
        elif self.kwargs:
            items.append('*')

        items.extend(self.kwargs)

        if self.varkwargs:
            items.append('**' + self.varkwargs)

        return ', '.join(items)

    def get_call_str(self):
        items = []

        items.extend(self.args)

        if self.varargs:
            items.append('*' + self.varargs)

        items.extend(kw + '=' + kw for kw in self.kwargs)

        if self.varkwargs:
            items.append('**' + self.varkwargs)

        return ', '.join(items)
