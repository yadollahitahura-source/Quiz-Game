from Example1 import z,add
import pytest
@pytest.mark.slow
def test_z():
    assert z(4) is True

@pytest.mark.parametrize(
    "a,b,result",
    [
        (1,2,3),
        (3,5,8),
        (100,200,300),
        (432,234,666),
    ]
)
def test_add(a,b,result):
    assert add(a,b)==result