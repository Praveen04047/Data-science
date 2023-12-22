# Importing a specific module from a package
import math
result = math.sqrt(25)
print(result)

# Importing a package with an alias
import numpy as np
arr = np.array([1, 2, 3])
print(arr)

# Importing specific functions or classes from a module
from math import sqrt
result = sqrt(25)
print(result)

# Importing everything from a module (not recommended for large modules)
from math import *
result = pow(2, 3)
print(result)