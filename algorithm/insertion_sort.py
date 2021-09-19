array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하며 반복
        if array[j] < array[j-1]: # 오른쪽 놓인 값보다 왼쪽에 놓인 값이 클 경우
            array[j], array[j-1] = array[j-1], array[j] # swap
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(array)