N = int(input())

bag_count = []

if (N % 5) % 3 == 0:
  bag_count.append((N // 5) + ((N % 5) / 3))
if (N % 3) % 5 == 0:
  bag_count.append((N // 3) + ((N % 3) / 5))

for i in range(0, (N//5)+1):
  for j in range(0, (N//3)+1):
    if N == 5*i + 3*j:
      bag_count.append(i + j)

if len(bag_count) == 0:
  bag_count.append(-1)

print(int(min(bag_count)))


