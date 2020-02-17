import numpy as np

from .figure import Figure
from .helper import get_z


class Pyramid(Figure):

    def __init__(self):
        super().__init__("Pyramid")

    def make_figure(self):
        ax = self.ax

        # Face 1
        x1 = np.array([[-1, -1, 1, 1, -1],
                       [0, 0, 0, 0, 0]])
        y1 = np.array([[-1, 1, 1, -1, -1],
                       [0, 0, 0, 0, 0]])
        z1 = np.array([[-1, -1, -1, -1, -1],
                       [1, 1, 1, 1, 1]])

        # Face 2
        x2 = np.array([[0, 0, 1, 0],
                       [0, 0, 0, 0]])
        y2 = np.array([[0, 1, 1, 0],
                       [0, 0, 0, 0]])
        z2 = np.array([[0, 0, 1, 0],
                       [0, 0, 0, 0]])
        # Face 3
        x3 = np.array([[1, 1, 0.5, 1],
                       [1, 1, 1, 1]])
        y3 = np.array([[0, 1, 0.5, 0],
                       [0, 0, 0, 0]])
        z3 = np.array([[0, 0, 1, 0],
                       [0, 0, 0, 0]])
        # Face 4
        x4 = np.array([[0, 1, 0.5, 0],
                       [0, 0, 0, 0]])
        y4 = np.array([[1, 1, 0.5, 1],
                       [1, 1, 1, 1]])
        z4 = np.array([[0, 0, 1, 0],
                       [0, 0, 0, 0]])
        # Face 5
        x5 = np.array([[1, 0, 0.5, 1],
                       [1, 1, 1, 1]])
        y5 = np.array([[0, 0, 0.5, 0],
                       [0, 0, 0, 0]])
        z5 = np.array([[0, 0, 1, 0],
                       [0, 0, 0, 0]])

        ax.plot_surface(x1, y1, z1, alpha=0.75, color="navy")

        # ax.plot_surface(x2, y2, z2, alpha=0.75, color="navy")
        # ax.plot_surface(x3, y3, z3, alpha=0.75, color="navy")
        # ax.plot_surface(x4, y4, z4, alpha=0.75, color="navy")
        # ax.plot_surface(x5, y5, z5, alpha=0.75, color="navy")

        ax.plot3D([0, 0], [0, 1], [1, 1], color="red", linewidth=6, alpha=1)
        ax.plot3D([0, 0], [1, 1], [1, -1], color="red", linewidth=6, alpha=1)

        ax.scatter3D([0, 0, 0], [0, 1, 1], [1, 1, -1], color="k", s=12, alpha=1)
        return ax

    def get_s(self, p1, p2, p3):
        try:
            fp1 = float(p1.strip())
            fp2 = float(p2.strip())
            s = fp1 * (fp1 + 2 * fp2)
            return str(s)
        except:
            return super().get_s(p1, p2, p3)

    def get_v(self, p1, p2, p3):
        try:
            fp1 = float(p1.strip())
            fp2 = float(p2.strip())
            v = fp1 * fp1 * fp2 / 3
            return str(v)
        except:
            return super().get_v(p1, p2, p3)

    @property
    def has_p2(self):
        return True
