import matplotlib.pyplot as plt 
import numpy as np 
import cmath

x = int(input("Enter the real number of the equation: "))
y = int(input("Enter the imaginary number of the equation: "))
print(complex(x + 1j*y))

x1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) 
y1 = x1 + 1j
  
plt.plot(x, y) 
plt.xlabel("Real") 
plt.ylabel("Imaginary") 
plt.title("Solving Complex Equations") 
plt.show()  
plt.figure() 
x1 = [2, 4, 6, 8] 
y1 = [3, 5, 7, 9] 
plt.plot(x1, y1, '-.') 
plt.show() 