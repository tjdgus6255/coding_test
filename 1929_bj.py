import sys
M, N = map(int, sys.stdin.readline().split())

for i in range(M, N+1):
  prime_check = 'o'
  for j  in range(2, i):
    if prime_check == 'x':
      break
    else:
      if i % j == 0:
        prime_check = 'x'
        break
  if prime_check == 'o' and i != 1:
      print(i)

# 초기 코드
#################################################
     
import sys
M, N = map(int, sys.stdin.readline().split())

def prime_check(num):
  if num == 1:
    return False
  else:
    for j in range(2, int((num**0.5)+1)):
      if num % j == 0:
        return False
    return True

for i in range(M, N+1):
  if prime_check(i):
    print(i)

# 최종본
###################################################
# 시간 초과를 어떻게 해결해야 하나 고민해보았지만
# 답이 나오지 않아 블로그를 참고하였습니다.
# 제곱근까지만 계산해도 된다는 것을 알았습니다. 