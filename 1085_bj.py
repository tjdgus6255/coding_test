import sys
x, y, w, h = map(int, sys.stdin.readline().split())

distance_list = [x, y, w-x, h-y]

distance = 1001
for i in distance_list:
  if distance > i:
    distance = i

print(distance)

# min 쓰세요 그냥 ㅎㅎ 