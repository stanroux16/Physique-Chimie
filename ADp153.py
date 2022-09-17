import matplotlib.pyplot as plt
import numpy as np


dt = 3 * 24 * 60 * 60
r = 384000000

x = np.array([1, 0.79, 0.17, -0.51, -0.99, -0.99, -0.51, 0.17, 0.79])*r
y = np.array([0.00, 0.62, 0.92, 0.82, 0.33, -0.33, -0.82, -0.92, -0.62])*r

def vecteur_vitesse(x, y, dt, i):
    vx = (x[i+1] - x[i-1]) / (2*dt)
    vy = (y[i+1] - y[i-1]) / (2*dt)
    plt.quiver(x[i], y[i], vx, vy, angles="xy", scale_units="xy", scale=0.00001, color="red")

plt.plot(x, y, "bo")
vecteur_vitesse(x, y, dt, 0)
vecteur_vitesse(x, y, dt, 1)
vecteur_vitesse(x, y, dt, 2)
vecteur_vitesse(x, y, dt, 3)
vecteur_vitesse(x, y, dt, 4)
vecteur_vitesse(x, y, dt, 5)
vecteur_vitesse(x, y, dt, 6)
vecteur_vitesse(x, y, dt, 7)
plt.title("Trajectoire de la lune")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.axis("scaled")

a = np.linspace(0, 2*np.pi, 100); x2 = np.cos(a)*r*1.06; y2 = np.sin(a)*r*0.93
plt.plot(x2, y2, "b--")
plt.show()