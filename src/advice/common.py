from .__external__ import AOPError


class AdviceError(AOPError):
    pass


class AdviceRuntimeError(AdviceError):
    pass
