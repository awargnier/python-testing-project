import pytest

def total_with_tip(bill,percentage):
  if(bill < 0):
    raise ValueError ("Bill should be positive")
  if(percentage < 0):
    raise ValueError ("Percentage should be positive")
  
  tip = percentage/100 * bill
  if(tip > 500):
    tip = 500

  total = bill + tip
  if total < 5:
    total = 5

  return round(total,2)

def test_classic():
  assert total_with_tip(100,20) == 120

def test_poor_service():
  assert total_with_tip(100,0) == 100

def test_tip_max():
  assert total_with_tip(5000,15) == 5500

def test_min_total():
  assert total_with_tip(4,10) == 5

def test_two_decimal():
  assert total_with_tip(10,2.33) == 10.23

def test_negative_error():
  with pytest.raises(ValueError) as exceptionTips:
    total_with_tip(100, -10)
  assert str(exceptionTips.value) == "Percentage should be positive"

  with pytest.raises(ValueError) as exceptionBill:
    total_with_tip(-10, 10)
  assert str(exceptionBill.value) == "Bill should be positive"