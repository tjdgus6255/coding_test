import sys
N, M = map(int, sys.stdin.readline().split())

under_m = list(map(int, sys.stdin.readline().split()))

near_m = []

for i in under_m:
  for j in under_m:
    for k in under_m:
      if i != j and i != k and j != k and (i+j+k) <= M:
        near_m.append(i+j+k)

print(max(near_m))
