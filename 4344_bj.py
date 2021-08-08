c = int(input())
list_score = [] 

for _ in range(c):
  input_things = list(map(int, input().split()))
  list_score = input_things[1:]
  avg = (sum(list_score) / len(list_score))
  count = 0
  for i in range(len(list_score)):
    if(list_score[i] > avg):
      count += 1
  print("%.3f"%((count/len(list_score))*100) + "%") 

# 내가 푼것
##########################################################

import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    data = input().strip().split(' ')
    scores = list(map(float, data[1:]))
    average = sum(scores) / len(scores)

    above = 0
    for score in scores:
        if score > average:
            above += 1

    print(f'{(above/len(scores))*100:.3f}%')
# 남이 푼것

# sys 모듈 사용해보기
# format 사용해보기