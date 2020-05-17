import matplotlib.pyplot as plt
import numpy as np
from 数电.utils import *

# 5-2
plot = Plot()
plt.xlim(-2, 20)
plot("010101010101010101", "CLK")
plot("011001100110011110")
plot("000111100001111110")
plot("000000011111111001")
plot("000000000001100000", "$Z$")

plt.xticks([])
plt.yticks([])
plt.show()

# 5-3
plot = Plot()
plt.xlim(-2, 10)
plot("010101010", "CLK")
plot("000000000")
plot("000000000")
plot("000000000")

plt.xticks([])
plt.yticks([])
plt.show()

