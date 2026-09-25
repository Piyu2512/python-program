from numpy import array

# The ndim attribute

arr1 = array([1, 2, 3, 4, 5])
print(arr1.ndim)

arr2 = array([[1, 2, 3], [4, 5, 6]])
print(arr2.ndim)


#The shape attribute

arr1 = array([1, 2, 3, 4, 5])
print(arr1.shape)

arr2 = array([[1, 2, 3], [4, 5, 6]])
print(arr2.shape)


#The size attribute


arr1 = array([1, 2, 3, 4, 5])
print(arr1.size)

arr2 = array([[1, 2, 3], [4, 5, 6]])
print(arr2.size)


#The itemsize Attribute


arr1 = array([1, 2, 3, 4, 5])
print(arr1.itemsize)

arr2 = array([1.1,2.1])
print(arr2.itemsize)

#The dtype attribute

arr1 = array([1, 2, 3, 4, 5])
print(arr1.dtype)

arr2 = array([1.1,2.1,3.5,4,5.0])
print(arr2.dtype)


#the nbytes attribute

arr2 = array([[1,2,3],[4,5,6]])
print(arr2.nbytes)

