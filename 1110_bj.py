InputN = int(input())
count = 0
N = InputN
Ncycle = 0

while True:
  Ncycle = ((N % 10) * 10) + ((N // 10) + (N % 10))%10
  count += 1
  if InputN == Ncycle:
    break
  N = Ncycle
# 
print(count)