import numpy as np
from  matplotlib import pyplot as plt
from matplotlib import style            #style lib
style.use('ggplot')                     #style name

x = np.arange(0,4*np.pi,.1)             #nmap ranging
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,'g',label='sine',linewidth='5')
plt.plot(x,z,'r',label='cosine',linewidth='2')
plt.title("sine function")
plt.xlabel("x")
plt.ylabel("y = sin(x)")

plt.legend()
plt.grid('True')
plt.show()

