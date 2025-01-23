import numpy as np
import matplotlib.pyplot as plt

class minkowskiDiagram():
  def __init__(self, ax, line, line_hyp):
    self.ax = ax
    self.line = line
    self.line_hyp = line_hyp
    self.T,self.X = np.meshgrid(line, line)
  
  def plot_cones(self):
    self.ax.plot(self.line,self.line, color = 'green', linestyle = '--')
    self.ax.plot(self.line, -self.line, color = 'green', linestyle = '--')
    self.ax.fill_between(self.line, self.line, -self.line, color= 'gray', alpha = 0.6)
    self.ax.fill_between(self.line, -self.line, self.line, color = 'gray', alpha = 0.6)
  
  def plot_hyperbolas(self):
    xh1 = np.cosh(self.line_hyp)
    xh2 = -np.cosh(self.line_hyp)
    yh1 = np.sinh(self.line_hyp)
    yh2 = -np.sinh(self.line_hyp)

    self.ax.plot(xh1, yh1, color = 'red')
    self.ax.plot(xh2, yh2, color = 'red')
    self.ax.plot(yh1, xh1, color = 'purple')
    self.ax.plot(yh2, xh2, color = 'purple')
  
  def lorentz_transform(self, beta):
    gamma = 1/np.sqrt(1-beta**2)
    return np.array([[gamma, beta*gamma],[beta*gamma, gamma]])
  
  def grid(self):
    self.ax.plot(self.T,self.X, '-', color = 'gray', zorder = -1)
    self.ax.plot(self.X,self.T, '-', color = 'gray', zorder = -1)
  
  def coordinate_transform(self, og_array, beta):
    transformed_array = self.lorentz_transform(beta)@og_array
    return transformed_array
  
  def transformed_grid(self, beta):
    TX = np.array([self.T.reshape(-1), self.X.reshape(-1)])
    TX_transform = self.lorentz_transform(beta)@TX
    T_transform = TX_transform[0].reshape(self.T.shape)
    X_transform = TX_transform[1].reshape(self.X.shape)

    return T_transform, X_transform
  
  def plot_transformed_grid(self, beta):
    T_transform, X_transform = self.transformed_grid(beta)
    self.ax.plot(T_transform, X_transform, '-', color = 'black')
    self.ax.plot(X_transform, T_transform, '-', color = 'black')