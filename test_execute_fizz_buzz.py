import pytest

from execute_fizz_buzz import fizz_buzz


@pytest.mark.parametrize(
    ["test_num"],
    [[3], [6], [9], [12], [15], [18], [21], [24], [27]]
)

# test~と書いてあったら、pytestがテストの実行対象として認識してくれる
# 命名するときは「test_関数名_条件」
def test_fizz_buzz_multiple_of_3(test_num) -> None:
  # 準備（mockが入ることもある）
  # num = 3

  # 実行
  result = fizz_buzz(test_num)

  # 検証
  expected = "Fizz"
  assert result == expected
