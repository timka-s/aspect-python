class AdviceRuntime:
    def before(self):
        raise NotImplementedError

    def after(self, result):
        raise NotImplementedError

    def throw(self, error):
        raise NotImplementedError
