import pytest

def test_first():
    msg = 'Hello'
    assert msg == 'Hello', 'Test failed because strings do not match'

@pytest.mark.smoke
def test_second():
    a = 4
    b = 6
    assert a+2 == 6, 'Addition do not match'