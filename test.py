import numpy as np
import matplotlib.pyplot as plt 
from minkowski import minkowskiDiagram

fig, ax = plt.subplots(figsize = (6,6))
ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
ax.set_xlabel('x')
ax.set_ylabel('t')

def on_click(event):
  if event.inaxes:
    ax.plot(event.xdata, event.ydata, 'rx')
    fig.canvas.draw()
    print(f"Clicked at: ({event.xdata:.2f}, {event.ydata:.2f})")
    
t = np.linspace(-100,100,201)
t_hyp = np.linspace(-5,5,100)
mD = minkowskiDiagram(ax, t, t_hyp)
mD.plot_cones()
mD.plot_hyperbolas()
mD.grid()

fig.canvas.mpl_connect('button_press_event', on_click)
plt.show()