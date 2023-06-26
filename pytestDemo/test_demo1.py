import pytest


def test_firstProgram(setup):
    print("Hello")


@pytest.mark.smoke
def test_secondProgram():
    a = 4
    b = 6
    assert a + 2 == b, "Addition do not match"


