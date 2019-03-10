# Sugam Khetrapal

# import libraries
import numpy as np      # to calculate mean and median
from scipy import stats # to calculate mode

# take numeric input
n = input()

# take array input
integers_list = [int(i) for i in input().split()]

# print mean
print(np.mean(integers_list))

# print median
print(np.median(integers_list))

# print mode
ModeResult = stats.mode(integers_list)
mode = int(ModeResult[0])
print(mode)