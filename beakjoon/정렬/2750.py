'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다.
이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

예제 입력 1
5
5
2
3
4
1
예제 출력 1
1
2
3
4
5
'''

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input())) # 리스트에 입력한 수 담기

arr.sort() # 정렬

for i in range(n): # 정렬된 대로 하나하나 뽑아내기
    print(arr[i])

print('-'*50)

# merge sort
def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid]) # sort the left half of the array (assuming n > 1)
    right = merge_sort(array[mid:]) # sort the right half of the array (assuming n > 1)
    i,j,k = 0,0,0

    while i < len(left) and j < len(right): # i, j 가 가리키는 값 비교-> 작은 값을 k에 넣기
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

        if i == len(left): # 한쪽 리스트가 끝난 경우, 나머지 리스트를 넣어줌
            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1
        elif j == len(right):
            while j < len(left):
                array[k] = left[i]
                i += 1
                k += 1
        return array

n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array = merge_sort(array) # merge the two halves together

for data in array:
    print(data)


print('-'*50)

# Bubble sort
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in range(len(arr)):
    for j in range(len(arr)):
      if arr[i] < arr[j]:
          arr[i], arr[j] = arr[j], arr[i]

for m in arr:
    print(m)

print('-'*50)

# sys.stdin.readline()
# => input() 과 비교해서 prompt message을 인수로 받지 않고
# 개행 문제를 삭제하지 않기 때문에 더 빠름

import sys
a = sys.stdin.readline().strip()
arr = []

for _ in range(a):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for data in arr:
    print(data)