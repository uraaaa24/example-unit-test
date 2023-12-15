from .execute_fizz_buzz import fizz_buzz


# test~と書いてあったら、pytestがテストの実行対象として認識してくれる
# 命名するときは「test_関数名_条件」
def test_fizz_buzz_multiple_of_3() -> None:
  # 準備（mockが入ることもある）
  n = 3

  # 実行
  result = fizz_buzz(n)

  # 検証
  expected = "Fizz"

  assert result == expected
