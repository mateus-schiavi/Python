import matplotlib.pyplot as plt 
import numpy as np 
import cmath
import pytest

def test_one():
    data = np.arange(12) + 1j*np.arange(-4, 8) 
    x = data.real 
    y = data.imag 
    plt.plot(x, y, '-.r*') 
    plt.ylabel('Imaginary') 
    plt.xlabel('Real') 
    plt.show()

def test_two():
    data = np.array([1+5j, 2-1j, -1j, -8, 4+3j, 3+2j, -2+6j, 5]) 
    x = data.real 
    y = data.imag 
    plt.plot(x, y, 'g*') 
    plt.ylabel('Imaginary') 
    plt.xlabel('Real') 
    plt.show()
     
def test_three():
    data = np.arange(10) + 1j*np.arange(0,10)
    x = data.real
    y = data.imag
    plt.plot(x,y, 'g*')
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.show()
    

pytest.main(["-v", "--tb=line", "-rN", __file__]) 