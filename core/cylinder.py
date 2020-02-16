import numpy as np
from .figure import Figure


class Cylinder(Figure):

    def __init__(self):
        super().__init__("Cylinder")

    def make_figure(self):
        ax = self.ax

        # Cylinder
        x = np.linspace(-1, 1, 100)
        z = np.linspace(-1, 2, 100)

        xc, zc = np.meshgrid(x, z)
        yc = np.sqrt(1 - xc ** 2)

        # Draw parameters
        ax.plot_surface(xc, yc, zc, color="navy", alpha=0.75, rstride=20, cstride=10)
        ax.plot_surface(xc, -yc, zc, color="navy", alpha=0.75, rstride=20, cstride=10)

        ax.plot3D([0, 0], [0, 0], [-1, 2], color="red", linewidth=6, alpha=1)
        ax.plot3D([0, 0], [0, 1], [2, 2], color="red", linewidth=6, alpha=1)

        ax.scatter3D([0, 0, 0], [0, 0, 1], [-1, 2, 2], color="k", s=12, alpha=1)

        return ax

    def get_s(self, p1, p2):
        try:
            fp1 = float(p1.strip())
            fp2 = float(p2.strip())
            s = 2 * np.pi * fp1 * (fp1 + fp2)
            return str(s)
        except:
            return super().get_s(p1, p2)

    def get_v(self, p1, p2):
        try:
            fp1 = float(p1.strip())
            fp2 = float(p2.strip())
            v = np.pi * fp1 * fp1 * fp2
            return str(v)
        except:
            return super().get_v(p1, p2)
