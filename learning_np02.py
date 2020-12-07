import numpy as np

# shape : 배열의 크기를 알려준다.

# ZEROS, ONES, FULL ,EYE, RANGE

a = np.zeros((2,2)) # ZEROS : 2X2 의 행렬을 0으로 채움
print(a)

a = np.ones((2,3)) # ONES : 2x3 의 헁렬을 1 로 챼움
print(a)

a = np.full((2,3), 'm' ) # FULL : 2x3의 행렬을 m으로 채움 
print(a)

a = np.eye(4) # eye : 4x4의 행렬을 1을 대각선으로 채우고 나머지는 0을 채움.
print(a)

a = np.array(range(20)).reshape((4,5)) # range: 0-19의 숫자로 4x5 행렬
print(a)

# 슬라이싱 ---------------------

lst = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
arr = np.array(lst)

a = arr[0:2, 0:2]
print(a)
# 출력:
# [[1 2]
#  [4 5]]
 
a = arr[1:, 1:]
print(a)
# 출력:
# [[5 6]
#  [8 9]]


# 정수 인덱싱 ------------------
# (a[[row1, row2], [col1, col2]] )
lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
a = np.array(lst)
 
# 정수 인덱싱
s = a[[0, 2], [1, 3]]
 
print(s)
# 출력
# [2 12]