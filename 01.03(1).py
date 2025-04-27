import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,10.1,0.1)
y1 = x
y2 = 2*x
y3 = 3*x
y4 = x**2
y5 = 2*x**2

plt.plot(x, y1, label = 'y = x', color = 'blue')
plt.plot(x, y2, label = 'y = 2x', color = 'green')
plt.plot(x, y3, label = 'y = 3x', color = 'red')
plt.plot(x, y4, label = 'y = x^2', color = 'orange')
plt.plot(x, y5, label = 'y = 2x^2', color = 'black')

plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)
plt.show()


