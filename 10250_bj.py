import sys

T = int(sys.stdin.readline())

for _ in range(T):
  h, w, n = map(int, sys.stdin.readline().split())
  location = ((n-1) // h) + 1
  floor = n % h
  if(floor == 0): floor = h
  print(100*floor + location)

