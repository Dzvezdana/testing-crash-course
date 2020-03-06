import pytest
import canBuyBeer

def test_1():
  # give it non-string and check you get TypeError
  with pytest.raises(TypeError) as tErr:   
    canBuyBeer.checkId(123) 
  assert str(tErr.value) == 'Input needs to be a string'
    
def test_2():
  # give it a string and check you don't get TypeError
  canBuyBeer.checkId("123456789")
    
def test_checkId_raises_ValueError_for_non_numerical_values():
  with pytest.raises(ValueError):
    canBuyBeer.checkId("jen123456")
    
class TestCheckId:
    
  def test_4(self):
    # give it a string w/ numbers of length != 9 and check you get False
    pass
      
  def test_checkId_succeeds_for_valid_values(self):
    # give it a string w/ numbers of length == 9 and check you get True
    tmp1 = canBuyBeer.checkId("123456789")
    assert tmp1, "What the hell"
    #if not not tmp1:
    #    raise AssertionError()
      
  def test_6(self):
    # give it a string w/ numbers and check you don't get ValueError
    try:
      canBuyBeer.checkId("a234123412")
    except ValueError:
      #assert False
      pytest.fail("Boom")
      