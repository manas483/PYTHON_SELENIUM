import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("I will execute in fixture demo ")

    def test_fixtureDemo1(self):
        print("I will execute in fixture demo1 ")

    def test_fixtureDemo2(self):
        print("I will execute in fixture demo 2")

    def test_fixtureDemo3(self):
        print("I will execute in fixture demo3 ")
