"""
S' = -beta*S*I
I' = beta*S*I - nu*I
R' = nu*I
"""
import numpy as np
from ODESolver import ForwardEuler
from matplotlib import pyplot as plt
class SIR:
    def __init__(self, nu, beta,S0,I0,R0):
        if isinstance(nu, (float,int)):
            #Is number?
            self.nu = lambda  t: nu
        elif callable(nu):
            self.nu = nu
        if isinstance(beta, (float, int)):
            # Is number?
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta

        self.initial_conditions = [S0, I0, R0]
    def __call__(self, u, t):
        S, I, _ = u

        return  np.asarray([
            -self.beta(t)*S*I,#Succeptibles
             self.beta(t)*S*I - self.nu(t)*I , #Infected
             self.nu(t)*I #Recovered


        ])

if __name__ == "__main__":

    beta = lambda  t: 0.0005 if t<=25 else 0.0001
  
    #(self, nu, beta,S0,I0,R0):
    sir = SIR(0.6, beta, 4500000, 3052,  1000)
    solver = ForwardEuler(sir)

    solver.set_inital_conditions(sir.initial_conditions)
    time_steps = np.linspace(0, 51, 1001 )
    u, t = solver.solve(time_steps)
    plt.plot(t,u[:,0], label = "Susceptible")
    plt.plot(t,u[:,1], label = "Infected")
    plt.plot(t,u[:,2],label = "Recovered")
    plt.legend()
    plt.show()