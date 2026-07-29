import numpy as np

a = np.array([1,2,3,4,5])
print(a)

print(type(a))


b = np.array([[1,2,3], [4,6,7], [7,8,9]])

print(b[1][0])
print(b[1,0])

print(b.shape)
print(b.ndim)
print(b.size)
print(b.dtype)


c = np.array([[1,2,3], [4,"hello my name is utkarsh",7], [7,8,9]])
print(c.dtype)
print(type(c[1][1]))



# arrays with default values 

a1 = np.full((2,3,4), 1)


a2 = np.zeros(10,3,4)


#arange, linspace 
