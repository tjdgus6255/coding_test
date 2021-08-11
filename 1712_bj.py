import sys
a, b, c = map(int, sys.stdin.readline().split())

if b < c:
  print(int(a / (c - b) + 1))
else:
  print(-1) 

####################################################

# 시간 초과가 자꾸 떠서 다른 분들의 코드를 보았습니다.
# 코드를 보고 이해는 했으나 막상 이런 문제가 다시 나왔을때
# 풀 수 있을지 모르겠네요;;
