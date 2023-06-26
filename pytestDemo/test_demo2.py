import pytest


@pytest.mark.smoke
# @pytest.mark.skip
@pytest.mark.xfail
def test_secondCreditCardProgram():
    msg = "Hello"
    assert msg == "Hi", "Match not found"
