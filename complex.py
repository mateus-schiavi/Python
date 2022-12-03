import matplotlib.pyplot as plt 
import numpy as np 
import cmath

x = int(input("Enter the real number of the equation: "))
y = int(input("Enter the imaginary number of the equation: "))
print(complex(x + 1j*y))
 
plt.plot(x, y, '-.') 
plt.ylabel("Imaginary")
plt.xlabel("Real") 
plt.title("Solving Complex Equations") 
plt.show()  
