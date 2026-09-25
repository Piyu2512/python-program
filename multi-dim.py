#------Multi Dimensional array--------#

from numpy import array


#The array() function

a=array([1,2,3,4])
print(a)

a=array([[1,2,3,4],[5,6,7,8]])
print(a)


from numpy import ones, zeros

# Ones and zeros()

a = ones((3,4), float)
print(a)

b = zeros((3,4), int)
print(b)


from numpy import eye

# eye()

a = eye(3)
print(a)
from numpy import array, reshape

# reshape

a = array([1,2,3,4,5,6])
print(a)

b = reshape(a, (2,3))
print(b)

a = array([0,1,2,3,4,5,6,7,8,9,10,11])

b = reshape(a, (2,3,2))
print(b)

b = reshape(a, (3,2,2))
print(b)

