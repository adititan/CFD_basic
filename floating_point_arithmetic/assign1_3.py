import numpy as np
import matplotlib.pyplot as plt

def func(x):
    print(x,1.0-np.cos(x))
    return (1.0-np.cos(x))/x**2

def factorial(n):
    result = 1;
    for i in range(1,n+1):
        result *= i
    return result 

def exact_func(x,n):
    summ = 0.0
    for i in range(2,n):
        summ += (-1)**(i+1) * x**(2*i-2)/factorial(2*i)
    summ += 0.5
    return summ

def plot(x1,x2,length):
    x = np.linspace(x1,x2,length)
    approx = [func(x[i]) for i in range(len(x))]
    exact  = [exact_func(x[i],50) for i in range(len(x))]
    plt.figure()
    plt.plot(x,approx,label = 'approx')
    plt.plot(x,exact,label = 'exact')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('func')
    plt.title("Plot of (1-cos(x))/x**2 near zero")
    plt.grid(True)
    plt.savefig('three.png')

plot(-4e-8,4e-8,1000)
