N = int(input())

move = []
def hanoi(num, start, end, other):
  if num == 0:
    return
  hanoi(num - 1, start, other, end)
  move.append((start, end))
  hanoi(num - 1, other, end, start)

hanoi(N, 1, 3, 2)
   
print(len(move))

for i, j in move:
  print(i, j)