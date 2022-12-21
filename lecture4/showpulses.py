# from commlib import default_pulse
import numpy as np
import matplotlib.pyplot as plt
from commlib import time_axis, default_pulse

Tmax = 6
N = 1024
TS = 3
t = time_axis(Tmax, N)
p = default_pulse(t, TS)
plt.plot(t, p)