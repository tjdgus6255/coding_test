M = int(input())
N = int(input())

prime_min = 10001
prime_sum = 0

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
    prime_sum += i
    if prime_min > i:
      prime_min = i

if prime_sum == 0:
  print(-1)  
else:
  print(prime_sum)
  print(prime_min)

    
     