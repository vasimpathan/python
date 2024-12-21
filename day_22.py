
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)


arr = np.array([1, 2, 3, 4, 5, 6])
arr[0:3]
arr.shape
arr.reshape((2,3))
#array([[1, 2, 3],
#       [4, 5, 6]])

arr + 1
# array([2, 3, 4, 5, 6, 7])

m1 = np.array([[1,2], [3,4]])
m2 = np.array([[5,6], [7,8]])
np.dot(m1, m2)
#array([[19, 22],
#       [43, 50]])

np.mean(arr)
#3.5

np.std(arr)
#1.707825127659933

np.random.rand(10)

#array([0.25393672, 0.50178933, 0.99858148, 0.71526973, 0.79330476,
#       0.9243129 , 0.65910974, 0.65514755, 0.93459802, 0.99812722])

arr = [1, 2, 3, np.nan, 5, 6]
#[1, 2, 3, nan, 5, 6]

np.isnan(arr)
#array([False, False, False,  True, False, False])

import time
ls1 = list(range(100000000))
start = time.time()
sum(ls1)
end = time.time()
print(end - start)
#1.1346824169158936

ls1 = np.array(ls1)
start = time.time()
np.sum(ls1)
end = time.time()
print(end - start)