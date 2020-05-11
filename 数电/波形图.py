import matplotlib.pyplot as plt
import numpy as np
from itertools import chain


class Plot(object):
    # t = range(40)
    # t = list(chain.from_iterable(zip(t, t)))
    _t = [0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7,
          8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14,
          15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21,
          21, 22, 22, 23, 23, 24, 24, 25, 25, 26, 26, 27, 27,
          28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 33, 33, 34,
          34, 35, 35, 36, 36, 37, 37, 38, 38, 39, 39]

    def __init__(self, name="$Q_{{{}}}$"):
        self.name = name
        self.n = 0
        self.loc = 0

    def __call__(self, time_series, name=None):
        if name is None:
            name = self.name.format(self.n)
            self.n += 1
        _y = list(map(int, time_series))
        _y = np.array(list(chain.from_iterable(zip(_y, _y))))
        print(name, self.n)
        _t = self._t[:len(_y)]
        plt.text(-1.5, self.loc + 0.5, name)
        plt.plot(_t, _y + self.loc)
        self.loc -= 1.2


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
