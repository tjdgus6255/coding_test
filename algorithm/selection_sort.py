array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]: # 현재 가장 작은 원소로 지정된 것보다 더 작은 원소가 존재한다면
            min_index = j # 인덱스를 교체
    array[i], array[min_index] = array[min_index], array[i] # swap

print(array)