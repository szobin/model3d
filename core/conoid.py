import numpy as np

from .figure import Figure


class Conoid(Figure):

    def __init__(self):
        super().__init__("Conoid")

    def make_figure(self):
        ax = self.ax

        # Set up the grid in polar
        theta = np.linspace(0, 2 * np.pi, 90)
        r = np.linspace(-1, -0.2, 50)
        T, R = np.meshgrid(theta, r)

        # Then calculate X, Y, and Z
        X = R * np.cos(T)
        Y = R * np.sin(T)
        Z = 2 + R * 3  # 3-np.sqrt(X ** 2 + Y ** 2) # - 1

        ax.plot_surface(X, Y, Z, color='navy', alpha=0.8)

        ax.plot3D([0, 0], [0, 1], [1.4, 1.4], color="red", linewidth=6, alpha=1)
        ax.plot3D([0, 0], [1, 1], [1.4, -1], color="red", linewidth=6, alpha=1)

        ax.scatter3D([0, 0, 0], [0, 1, 1], [1.4, 1.4, -1], color="k", s=12, alpha=1)

        return ax

    def get_s(self, p1, p2):
        try:
            fp1 = float(p1.strip())
            fp2 = float(p2.strip())
            s = np.pi * fp1 * (fp1 + fp2)
            return str(s)
        except:
            return super().get_s(p1, p2)

    def get_v(self, p1, p2):
        try:
            fp1 = float(p1.strip())
            fp2 = float(p2.strip())
            v = np.pi * fp1 * fp1 * fp2 / 3
            return str(v)
        except:
            return super().get_v(p1, p2)

