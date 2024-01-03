from classes.tips import total_with_tips, NegativeValueError
import pytest


def test_poor_service () :
    assert total_with_tips(100,0) == 100

def test_cheap_bill () :
    assert total_with_tips(2.30,20) == 5

def test_normal_bill () :
    assert total_with_tips(100,20) == 120

def test_expensive_bill () :
    assert total_with_tips(5000,15) == 5500

def test_cents () : 
    assert total_with_tips(10,33.3333) == 13.33

def test_negative_error () :
    with pytest.raises(NegativeValueError) as exceptionBill :
        total_with_tips(-4,20)
    assert str(exceptionBill.value) == "bill should be positive"

    with pytest.raises(NegativeValueError) as exceptionTip :
        total_with_tips(4,-20)
    assert str(exceptionTip.value) == "percentage should be positive"