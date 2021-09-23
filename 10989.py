import sys

def counting():
  N = int(input())

  num_list = [0]*(10001) # 최대 입력가능 숫자 + 1
  for _ in range(N):        
    num = int(sys.stdin.readline())  # N회 동안 num을 입력 받음
    num_list[num] += 1  # num_list에서 입력 받은 num에 해당하는 인덱스에 1씩 추가함

  for i in range(len(num_list)): # 10001번 동안 시행
    if num_list[i] != 0: # 해당 인덱스에 위치한 값이 0이 아닌 경우
      for _ in range(num_list[i]):  # 해당 인덱스에 위치한 값만큼 인덱스 값을 출력
        sys.stdout.write(str(i)+"\n") # 인덱스 값은 입력받은 데이터 값과 동일

def main(): # main에서 counting 실행
  counting()

if __name__ == '__main__': # main 함수가 위치한 곳일 경우에만 main 실행
  main()

#########################################################################
