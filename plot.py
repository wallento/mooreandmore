#!/usr/bin/python

import numpy as np
from matplotlib import pyplot as plt
data = np.genfromtxt('raw_data.csv', skip_header=1, delimiter=';', names = ['Year', 'Transistors', 'Frequency', 'PowerDensity', 'Cores'] )

fig = plt.figure(figsize=(8,5))

plt.semilogy(data['Year'], data['Transistors'], 'bs', label="Transistors")
plt.semilogy(data['Year'], data['Frequency'], 'rv', label="Frequency")
plt.semilogy(data['Year'], data['PowerDensity'], 'gx', label="Power Density")
plt.semilogy(data['Year'], data['Cores'], 'ko', label="Cores")

plt.ylim(ymin=1)
plt.grid()

plt.legend(loc="upper left")

plt.show()
