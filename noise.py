"""https://qsm.quantumtinkerer.tudelft.nl/1_basics_of_noise/"""
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 1
ts = np.linspace(0, 100, 100)
vs = np.asarray([np.random.normal(mu, sigma) for t in ts])

plt.plot(ts, vs)
plt.title("Signal")
plt.xlabel("Time (s)")
plt.ylim(-3, 3)
plt.ylabel("Voltage (mV)")
plt.show()
