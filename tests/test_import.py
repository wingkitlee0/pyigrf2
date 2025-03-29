import pyigrf2


def test_0001():
    print(pyigrf2._igrf.__dict__)
    print(pyigrf2.igrf14syn.__doc__)

    assert True


def test_0002():
    x, y, z, f = pyigrf2.igrf14syn(0, 2024.0, 1, 1, 0, 0)

    assert x * y * z * f != 0
