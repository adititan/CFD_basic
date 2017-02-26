import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from copy import deepcopy

def initialize_grid(x_max,x_min,time,cfl,a,N):
    dx = (x_max - x_min) /(N-1)
    dt = cfl/a*dx 
    n_iter = int((time/dt) - 0.5) + 1
    phi = [[0.0 for _ in range(N)] for _ in range(n_iter)]
    return phi,n_iter

def set_boundary_conditions( phi, N, at_t_0, at_x_0):
    phi[0] = at_t_0
    for i in range(len(at_x_0)):
        phi[i][0] = at_x_0[i]
    return phi

def do_FTCS(phi,n_iter,N,cfl,periodicity = None):
    for t in range(1,n_iter):
        for i in range(1,N-1):
            phi[t][i]= phi[t-1][i] -cfl*(phi[t-1][i+1] - phi[t-1][i-1])/2.0
    return phi

def do_FTFS(phi,n_iter,N,cfl,periodicity = None):
    for t in range(1,n_iter):
        for i in range(1,N-1):
            phi[t][i]= phi[t-1][i] -cfl*(phi[t-1][i+1] - phi[t-1][i])
    return phi
    
def do_FTBS(phi,n_iter,N,cfl,periodicity = None):
    for t in range(1,n_iter):
        for i in range(1,N-1):
            phi[t][i]= phi[t-1][i] -cfl*(phi[t-1][i] - phi[t-1][i-1])
        if periodicity == "yes":
            phi[t][0] = phi[t][N-2]
            phi[t][N-1] = phi[t][1]
    return phi

def do_FTCS2(phi,n_iter,N,cfl,periodicity = None):
    for t in range(1,n_iter):
        for i in range(1,N-1):
            phi[t][i]= phi[t-1][i] -cfl*0.5*(phi[t-1][i+1] - phi[t-1][i-1]) + cfl**2*0.5*(phi[t-1][i+1] + phi[t-1][i-1] - 2*phi[t-1][i])
        if periodicity == "yes":
            phi[t][0] = phi[t][N-2]
            phi[t][N-1] = phi[t][1] 
    return phi

def animate(phi,x,scheme,cfl,time,string,periodicity=None):
    plt.figure()
    for k in range(5):
        t = k/4.0*time
        i = int(len(phi)/4.0)*k
        if periodicity == None:
            plt.plot(x,phi[i], label = "t = " + str(t)+" sec")
        else:
            plt.plot(x, phi[i][1:-1], label = "t = " + str(t)+" sec")   
    plt.xlabel("x")
    plt.ylabel("u")
    plt.legend(loc = "best")
    plt.savefig(string + "_"+ str(scheme)[13:17]+"_"+ str(int(cfl*10))+ "_"+ str(int(time))+".png")

def question1(N,cfl,a,func):
    phi,n_iter = initialize_grid(1.0,0.0,1.0,cfl,a,N)
    set_boundary_conditions(phi,N,[0.0]*(N),[1.0]*n_iter)
    func(phi,n_iter,N,cfl)
    x = np.linspace(0.0,1.0,N)
    animate(phi,x,func,cfl,1.0,"q1")
    return phi

def question2(N,cfl,a,func,var = 0.0):
    phi,n_iter = initialize_grid(1.0,0.0,1.0,cfl,a,N)
    xi = np.linspace(0.0,1.0,N) 
    sine  = [ np.sin(2.0*np.pi*xi[i]) + var*np.sin(20.0*np.pi*xi[i]) for i in range(N)]
    set_boundary_conditions(phi,N,sine,[0.0]*n_iter)
    func(phi,n_iter,N,cfl)
    animate(phi,xi,func,cfl,1.0,"q2_"+ str(int(var)))
    return phi

def question3_a(N,cfl,a,func,time):
    phi,n_iter = initialize_grid(1.0,-1.0,time,cfl,a,N+2)
    xi = np.linspace(-1.0,1.0,N)
    sine = [0.0]*(N+2) 
    for i in range(N):
        sine[i+1]  = -np.sin(np.pi*xi[i])
    sine[0] = sine[N]
    sine[N+1] = sine[0]
    set_boundary_conditions(phi,N+2,sine,[0.0]*n_iter)
    func(phi,n_iter,N+2,cfl,"yes")
    animate(phi,xi,func,cfl,time,"q3a",periodicity = "yes")
    return phi

def question3_b(N,cfl,a,func,time):
    phi,n_iter = initialize_grid(1.0,-1.0,time,cfl,a,N+2)
    xi = np.linspace(-1.0,1.0,N)
    ic = [0.0]*(N+2) 
    for i in range(N):
        if abs(xi[i]) < 1.0/3.0:
            ic[i+1]  = 1.0
    ic[0] = ic[N]
    ic[N+1] = ic[0]
    set_boundary_conditions(phi,N+2,ic,[0.0]*n_iter)
    func(phi,n_iter,N+2,cfl,"yes")
    animate(phi,xi,func,cfl,time,"q3b_"+str(N),periodicity = "yes")
    return phi

if __name__ == '__main__':
    #Question 1
    phi = question1(50,0.4,1.0,do_FTCS)
    phi = question1(50,0.4,1.0,do_FTFS)
    phi = question1(50,0.4,1.0,do_FTBS)
    phi = question1(50,1.0,1.0,do_FTCS)
    phi = question1(50,1.0,1.0,do_FTFS)
    phi = question1(50,1.0,1.0,do_FTBS)
    phi = question1(50,1.5,1.0,do_FTCS)
    phi = question1(50,1.5,1.0,do_FTFS)
    phi = question1(50,1.5,1.0,do_FTBS)
    #Question 2(i)
    phi = question2(100,0.5,1.0,do_FTCS)
    phi = question2(100,0.5,1.0,do_FTFS)
    phi = question2(100,0.5,1.0,do_FTBS)
    #Question 2(ii)
    phi = question2(100,0.5,1.0,do_FTCS,1.0)
    phi = question2(100,0.5,1.0,do_FTFS,1.0)
    phi = question2(100,0.5,1.0,do_FTBS,1.0)
    #Question3(i)
    phi = question3_a(40,0.8,1.0,do_FTCS2,30.0)
    phi = question3_a(40,0.8,1.0,do_FTBS,30.0)
    #Question3(ii)
    phi = question3_b(40,0.8,1.0,do_FTCS2,4.0)
    phi = question3_b(40,0.8,1.0,do_FTBS,4.0)
    #Question3(iii)
    phi = question3_b(600,0.8,1.0,do_FTCS2,4.0)
    phi = question3_b(600,0.8,1.0,do_FTBS,4.0)
    phi = question3_b(600,0.8,1.0,do_FTCS2,40.0)
    phi = question3_b(600,0.8,1.0,do_FTBS,40.0)
