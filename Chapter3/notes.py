# Array Basics
import numpy as np

a = np.array([1,2,3,4.1])
print(a) #[1,2,3,4]
print(a.shape) #(4,)
print(a.dtype) #int64

b = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(b)

# Zeros
x = np.zeros((2,3,4))
print(x)

# Ones
x = np.ones((2,3,4))
print(x)

# Constants - This will make all 3's
x = 3*np.ones((2,3,4))
print(x)

# arange

y = np.arange(21)
z = y.reshape((3,7)) #rearranges the matrix with this shape
print(z)