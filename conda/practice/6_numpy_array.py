#1 1차원 리스트를 넘파이로
#2 2차원 리스트를 넘파이로
#3 3차원 리스트를 넘파이로

#1 1차원 리스트를 넘파이로

# import numpy as np

# temp_list = [1,3,5,7,9]
# temp_np_array = np.array(temp_list)

# print(temp_list, type(temp_list), len(temp_list))
# print(temp_np_array, type(temp_np_array), len(temp_np_array), temp_np_array.shape)

#2 2차원 리스트를 넘파이로

# import numpy as np

# temp_list = [[1,3,5,7,9], [2,4,6,8,10]]
# temp_np_array = np.array(temp_list)

# print(temp_list, type(temp_list), len(temp_list))
# print(temp_np_array, type(temp_np_array), len(temp_np_array), temp_np_array.shape)

#3 3차원 리스트를 넘파이로

# import numpy as np

# temp_list = [[1,3,5,7,9], [2,4,6,8,10], [1,1,1,1,1]]
# temp_np_array = np.array(temp_list)

# print(temp_list, type(temp_list), len(temp_list))
# print(temp_np_array, type(temp_np_array), len(temp_np_array), temp_np_array.shape)

import numpy as np

list_1 = [[1,2,3,4,5], [6,7,8,9,10]]
list_2 = [[11,12,13,14,15]]
list_3 = [[16,17,18,19,20]]

array_1 = np.array(list_1)
array_2 = np.array(list_2)

array_combine = np.concatenate([array_1, array_2, list_3], axis=0)
print(array_combine, array_combine.shape)

print(array_combine[0])
print(array_combine[0].sum())

print(array_combine[3,:])
print(array_combine[3,:].sum())

print(array_combine[:,0])
print(array_combine[:,0].sum())

print(array_combine[:,2])
print(array_combine[:,2].sum())
