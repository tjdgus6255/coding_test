N = int(input())

def factorial(number):
  if number == 0 or number == 1:
    return 1
  else:
    return number * factorial(number-1)

print(factorial(N))

# factorial은 식을 하도 많이 봐서 외었어요 ㅎㅎ