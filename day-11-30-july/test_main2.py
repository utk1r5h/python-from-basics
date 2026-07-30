from main2 import add, divide
import pytest 


def test_add():
  assert add(1,2)==3, "sum of 1 and 2 must be 3"
  assert add(-1,1) ==0, "sum of 1 and -1 must be 0"

def test_divide():
  with pytest.raises(ValueError, match= "Can not divide by zero"):
    divide(10,0)


# @pytest.fixture -->is something u can have run before every single test
# 