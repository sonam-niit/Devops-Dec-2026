import numpy as np 

arr1= np.array([1,2,3,4,5])
print(arr1)

print("sum: ",np.sum(arr1))
print("Mean: ",np.mean(arr1))
print("Min: ",np.min(arr1))
print("Max: ",np.max(arr1))
print("std: ",np.std(arr1))

arr2=np.array([[1,2,3],[4,5,6]])
print(arr2)

arr3=arr2.reshape(3,2)
print(arr3)