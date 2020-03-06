import impl
import pytest

FULL_BOARD_CONFIG = 'xoxoxxoxo'

def test_tic_tac_toe_check_x_based_winning_pattern():
  tmp1 = list(FULL_BOARD_CONFIG)
  tmp1[6] = 'x'
  assert impl.tic_tac_toe_check(tmp1) ==  'x', "fails to recognize x based winning pattern"
