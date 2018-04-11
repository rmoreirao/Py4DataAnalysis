import numpy as np

def printNpArrayAttr(npArray):
    print(npArray)
    print(npArray.ndim)
    print(npArray.shape)
    print(npArray.dtype)

array1 = [1,2,3,4.5]
npArray1 = np.array(array1)
printNpArrayAttr(npArray1)

array2 = [[1,2,3,4],[5,6,7,8]]
npArray2 = np.array(array2)
printNpArrayAttr(npArray2)

# Array of 0's!!
print(np.zeros(10))

print(np.zeros((3,6)))

# 'New array', indeed not empty!
print(np.empty((2, 3, 2)))

# New array from 0 until N
print(np.arange(15))

#Forcing specific Data Type to NArray

arr1 = np.array([1, 2, 3], dtype=np.float64)
print(arr1.dtype)
arr2 = np.array([1, 2, 3], dtype=np.int32)
print(arr2.dtype)

# Operations between two arrays

arr = np.array([[1., 2., 3.], [4., 5., 6.]])

print(arr + arr)

print(arr * arr)

print(arr * 3)

# Single Dimension Array Selection!

arr = np.arange(10)
print(arr)
print(arr[5:8])
arr[5:8] = 12
print(arr)

# Multiple Dimension Array Selection!

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr2d[0][2]
arr2d[0, 2]

# Boolean Search

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print(names == 'Bob')
print(data)

print(data[names == 'Bob'])

print (data[names == 'Bob', 2:])


data[data < 0] = 0
print(data)

# Reshaping an array!

print(np.arange(32).reshape((8, 4)))

# np.where!

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
print(np.where(cond, xarr, yarr))

arr = np.random.randn(4, 4)
print(arr)
print(np.where(arr > 0,1,-1))
print(np.where(arr > 0,1,arr))

# Mathematical and Statistical Methods

arr = np.random.randn(5, 4)
print(arr.mean())
print(np.mean(arr))
print(arr.sum())

# Unique and Other Set Logic

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))

# saving data to disk!

arr = np.arange(10)
np.save('some_array', arr)
print(np.load('some_array.npy'))