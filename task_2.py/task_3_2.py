import numpy as np
from math import cos, tan, sqrt, radians
h = 100
a = radians(45)
b = radians(35)
g = 9.81
V = (g * h * np.tan(radians(35))**2 / 2 * np.cos(radians(45))**2 * (1 - np.tan(radians(35)) * np.tan(radians(35))) ** 0.5)
print(V)

import numpy as np
k = 1.38 * 10**(-23)
e = 1.6 * 10**(-19)
h = 1.054 * 10**(-34)
T = 200
E = 300
pi = 3.14
N = (2 / pi**0.5 * h**0.5 * (k * T)**(3/2) * e**(E / k*T) * E**(T/2))
print(N)