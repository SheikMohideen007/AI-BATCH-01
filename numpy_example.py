import numpy as np

numbers=[1,2,3,4,5]


# numpy_array=np.array([1,2,3,4,5])
# numpy_array_sample=np.array([2,3,4,5,6])
# print(numpy_array[1:4])
# print(numpy_array+numpy_array_sample)

# print('Normal list : ',numbers*2)
# print('Numpy array : ',numpy_array*2)
# array[100]=[0]

# print(np.zeros(5))
# print(np.ones((2,3)))


# print(np.arange(10))
# print(np.arange(1,10,2))

# numpy_array_3d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(numpy_array_3d.ndim)

# numpy_array_2d=np.array([[1,2,3],[4,5,6]])
# print(numpy_array_2d[1][1])

# print(numpy_array_2d.size)

# # print('Numpy array 2d : ', numpy_array_2d*2)

# print(numpy_array_2d.shape)

# print(numpy_array_2d.reshape(3,2))


# print(np.random.rand(5)) # 0 - 1

# print(np.random.randint(10,20,size=5)) # 10 - 19
# print(np.random.randint(10,20,size=(5,2))) # 10 - 19


# stacking
# a=np.array([1,2,3])
# b=np.array([4,5,6])

# print(np.hstack((a,b)))

#TODO : vstack()


#splitting
numpy_array=np.array([1,2,3,4,5,6])
print(np.split(numpy_array,3))

#TODO : create a 2d dimension array -> hsplit(), vsplit()


#statistical function
#mean, median, max, min, sum
marks=np.array([[70,80,90],[60,75,85]])