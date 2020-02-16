import numpy as np
import matplotlib.pyplot as plt

from .figure import Figure


class Ball(Figure):

    def __init__(self):
        super().__init__("Ball")

    def make_figure(self):
        ax = self.ax

        # Create a sphere
        r = 1
        phi = np.linspace(0, np.pi, 90)
        theta = np.linspace(0, 2*np.pi, 180)
        pp, tt = np.meshgrid(phi, theta)

        x = r * np.sin(pp) * np.cos(tt)
        y = r * np.sin(pp) * np.sin(tt)
        z = r * np.cos(pp)

        ax.plot_surface(x, y, z, cmap=plt.cm.YlGnBu_r, alpha=0.75)

        ax.plot([0, 0], [0, 0], [0, 1], color="red", linewidth=5)
        ax.scatter3D([0, 0], [0, 0], [0, 1], color="k", s=14)
        return ax

    def get_s(self, p1, p2):
        try:
            fp1 = float(p1.strip())
            s = 4* fp1 * fp1 * np.pi
            return str(s)
        except:
            return super().get_s(p1, p2)

    def get_v(self, p1, p2):
        try:
            fp1 = float(p1.strip())
            v = 4 * fp1 * fp1 * fp1 / 3
            return str(v)
        except:
            return super().get_v(p1, p2)
