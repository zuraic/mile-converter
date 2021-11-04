def add(*args):
    s = 0
    for n in args:
        s += n
    return s


print(add(1, 2, 3))


def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.model = kw["model"]
        self.make = kw.get("make")


my_car = Car(model="Jep")
print(my_car.make)
