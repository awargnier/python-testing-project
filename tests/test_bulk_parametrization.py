import pytest
from tests.test_tips import total_with_tip
@pytest.mark.parametrize("num1,num2,expectation", [
  (10,20,12),
  (100,20,120),
  (0,0,5)
])

def test_tip_bulk(num1,num2, expectation):
  assert total_with_tip(num1,num2) == expectation