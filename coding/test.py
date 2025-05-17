import numpy as np

import pandas as pd

a = np.array([1, 2, 3, 4, 2])

print(np.where(a == 3))
print(np.where(a == 3)[0][0])