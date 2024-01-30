import numpy as np
arr=np.array([[1,2,np.nan,4],[5,6,7,np.nan],[9,np.nan,np.nan,np.nan]])
print("The Missing data is:",np.isnan(arr))