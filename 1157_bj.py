word_input = input().lower()
word = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_count = [0 for i in range(26)]

for i in word_input:
  word_count[word.index(i)] += 1

if word_count.count(max(word_count)) >= 2:
  print("?")
else: 
  print(word[word_count.index(max(word_count))].upper())

# 내가 푼 것
##################################################################################

word = input().upper()
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
r = 0
cout = 0
for a in abc:
    temp = word.count(a)
    if temp != 0:
        if r < temp:
            r = temp
            count = a
        elif r == temp:
            count = '?'
print(count)

# 남이 푼 것

# 내가 한 것과 남이 한 것 비교해보기
# 쓸데없이 소문자 변환이 들어감
# 모든 문자에 대해 count를 정의함(word_count)
# 특히 for문에서 차이가 많이남