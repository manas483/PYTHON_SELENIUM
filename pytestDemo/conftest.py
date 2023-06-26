import pytest


@pytest.fixture(scope="class")
def setup():
    print("I Will be execute first")
    yield
    print("I will be execute last")

@pytest.fixture()
def dataLoad():
    print("User data creates")
    return ["Manas", "Ranjan", "manas@gmail.com"]
