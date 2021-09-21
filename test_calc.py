import main as m
import pytest

def test_soma():
    assert m.soma(1998,23)

def test_sub():
    assert m.sub(10,50)

def test_mult():
    assert m.mult(3,7)

def test_div():
    assert m.div(25, 5)

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        m.div(5,0)



