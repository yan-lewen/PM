
# plot a graph of the function f(x) = x^3
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-10, 10, 100)
y = x**3
plt.plot(x, y)
plt.title('Graph of f(x) = x^3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

