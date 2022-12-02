from m import M
class A(M):
    def __init__(self):
        self.__a = True
        M.__init__(self)
    def getSelfA(self):
        return f"A is { self.__a }"
