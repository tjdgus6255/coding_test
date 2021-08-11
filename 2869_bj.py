import sys

A, B, V = map(int, sys.stdin.readline().split())

day = int((V-A)/(A-B)) + 1

if (V-A) % (A-B) == 0:
  print(day)
else:
  print(day+1)

##################################################
# 알고보면 쉬운데 생각이 않나..ㅜ