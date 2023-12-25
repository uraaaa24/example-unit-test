import pytest

from execute_fizz_buzz import fizz_buzz


@pytest.mark.parametrize(
    ["test_num"],
    [[3], [6], [9], [12], [18], [21], [24], [27]]
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

def test_fizz_buzz_multiple_of_5() -> None:
  # 準備
  num = 5

  # 実行
  result = fizz_buzz(num)

  # 検証
  expected = "Buzz"
  assert result == expected

def test_fizz_buzz_multiple_of_3_5(mocker) -> None:
  # 準備
  num = 15
  mocker.patch("execute_fizz_buzz.execute_api", return_value={})

  # 実行
  result = fizz_buzz(num)

  # 検証
  expected = "FizzBuzz"
  assert result == expected
