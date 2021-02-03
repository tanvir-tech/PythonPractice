import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4*np.pi,.1)
y = np.sin(x)           # function


plt.plot(x,y)           # drawing plot

plt.title("sine function")
plt.xlabel("x")
plt.ylabel("y = sin(x)")


plt.grid('True')
plt.show()




