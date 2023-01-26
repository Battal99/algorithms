class Liquid1:
    def __init__(self, mass, temp=None):
        self.mass = mass
        self.temp = temp


class Liquid2(Liquid1):
    def __init__(self, mass, temp):
        super().__init__(mass, temp)


class Mixture(Liquid2, Liquid1):
    def __init__(self, liq1: Liquid1, liq2: Liquid2):
        self.liq1 = liq1
        self.liq2 = liq2

    def get_temp_mixture(self):
        q = self.liq1.mass * (self.liq2.temp - self.liq1.temp)
        return q


res = Mixture(Liquid1(15, 15), Liquid2(10, 20))

print(res.get_temp_mixture())


# print(res.__mro__)


class O:
    def method(self):
        print('I am O')


class A(O):
    def method(self):
        super().method()
        print('I am A')


class B(O):
    def method(self):
        super().method()
        print('I am B')


class C(A, B):
    def method(self):
        super().method()
        print('I am C')

# C().method()
