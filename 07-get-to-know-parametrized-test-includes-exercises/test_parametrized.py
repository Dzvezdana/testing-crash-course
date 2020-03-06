import src.main as main
import pytest

class TestPhysicalInfo:
  def setup_method(self):
    self.physical_info = main.PhysicalInfo()

  @pytest.mark.parametrize("input", [1,30,48])
  def test_set_height_valid_values_2(self, input):
    if input < 17 or input > 84:
      pytest.skip("skipping")
    try:
      self.physical_info.set_height(input)
    except ValueError as e:
      assert False
