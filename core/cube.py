import numpy as np

from .figure import Figure
from .helper import get_z

points = np.array([[-1, -1, -1],
                   [1, -1, -1],
                   [1, 1, -1],
                   [-1, 1, -1],
                   [-1, -1, 1],
                   [1, -1, 1],
                   [1, 1, 1],
                   [-1, 1, 1]])


class Cube(Figure):

    def __init__(self):
        super().__init__("Cube")

    def make_figure(self):
        ax = self.ax
        r = [-1, 1]
        x, y = np.meshgrid(r, r)

        ax.plot_surface(x, y, get_z(1, x, y), alpha=0.75, color="navy")
        ax.plot_surface(x, y, get_z(-1, x, y), alpha=0.95, color="cyan")

        ax.plot_surface(x, get_z(-1, x, y), y, alpha=0.75, color="navy")
        ax.plot_surface(x, get_z(1, x, y), y, alpha=0.95, color="cyan")

        ax.plot_surface(get_z(1, x, y), x, y, alpha=0.75, color="navy")
        ax.plot_surface(get_z(-1, x, y), x, y, alpha=0.95, color="cyan")

        xy = 1.05
        ax.plot3D([xy, xy], [xy, xy], [-1, 1], color="red", linewidth=6, alpha=1)
        ax.scatter3D([xy, xy], [xy, xy], [-1, 1], color="k", s=12, alpha=1)
        return ax

    def get_s(self, p1, p2):
        try:
            fp1 = float(p1.strip())
            s = fp1 * fp1 * 6
            return str(s)
        except:
            return super().get_s(p1, p2)

    def get_v(self, p1, p2):
        try:
            fp1 = float(p1.strip())
            v = fp1 * fp1 * fp1
            return str(v)
        except:
            return super().get_v(p1, p2)
