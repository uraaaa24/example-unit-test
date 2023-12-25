def fizz_buzz(num: int) -> str:
  if num % 3 == 0 and num % 5 == 0:
    fizz_buzz = "FizzBuzz"
    execute_api()
    return fizz_buzz
  if num % 3 == 0:
    return "Fizz"
  if num % 5 == 0:
    buzz = "Buzz"
    return buzz
  return str(num)

def execute_api() -> str:
  request = ""
  raise 
