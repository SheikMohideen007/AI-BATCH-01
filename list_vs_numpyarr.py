import numpy as np
import time

# normal_list=[85,92,78,100,88]

# numpy_array=np.array(normal_list)

# print('list type :', type(normal_list), normal_list)
# print('numpy array type :', type(numpy_array), numpy_array)

size=1000000

python_list=list(range(size)) # [0,1,2,3,....1000000-1]
numpy_array=np.arange(size) 

result_list=[]
start_time=time.time()
for x in python_list:
    result_list.append(x*2)

list_duration=time.time()- start_time

print(f"Python list computation time : {list_duration:.5f} seconds")


start_time=time.time()
array_result=numpy_array*2
array_duration=time.time()-start_time

print(f"Numpy array computation time : {array_duration:.5f} seconds")

faster=list_duration/array_duration
print(f'Numpy is {faster:.1f}x faster than standard python list')