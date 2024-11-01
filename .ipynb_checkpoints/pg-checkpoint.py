import numpy as np
import numpy.ma as ma

# Create a masked array
arr = np.array([1, 2, 3, 4, 5])
mask = [False, True, False, True, False]
masked_arr = ma.masked_array(arr, mask)

print(masked_arr)  # Output: [1 -- 3 -- 5]