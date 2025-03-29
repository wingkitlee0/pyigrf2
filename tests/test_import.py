import pyigrf

def test_0001():
    print(pyigrf._igrf.__dict__)
    print(pyigrf.igrf14syn.__doc__)

    assert False