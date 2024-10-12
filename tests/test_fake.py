from pytest import mark
import random

@mark.smoke
def test_1():
    actuall_result = random.randint(1, 10)
    assert actuall_result == 3