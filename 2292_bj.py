N = int(input())
N_former = 1
N_present = 1
N_count = 1
while N!= 1:
  if((N_former <= N) and (N <= N_present)):
    print(N_count)
    break
  else:
    N_former = N_present
    N_present += (N_count * 6)
    N_count += 1 

if N == 1:
  print(N_count)    

