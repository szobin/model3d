import numpy as np
from io import BytesIO
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from .helper import get_z


class Figure:

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @property
    def ax(self):
        fig = plt.figure()
        ax = Axes3D(fig)

        r = [-1.5, 1.5]
        # z = 1.02

        # x1 = np.array([[-w, w, w, -w],
        #                [-w, -w, -w, -w]])
        # y1 = np.array([[-w, -w, w, w],
        #                [-w, -w, -w, -w]])
        # z1 = np.array([[-z, -z, -z, -z],
        #                [-z, -z, -z, -z]])

        x, y = np.meshgrid(r, r)
        z = get_z(-1.02, x, y)
        ax.plot_surface(x, y, z, alpha=0.75, color="gray")

        return ax

    @staticmethod
    def get_image(ax):
        figure = ax.get_figure()
        figure_data = BytesIO()
        figure.savefig(figure_data, dpi=72)
        figure.clf()
        img = Image.open(figure_data)
        # return img
        return ImageTk.PhotoImage(img)

    def make_figure(self):
        return self.ax

    def image3d(self, angle):
        ax = self.make_figure()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.xaxis.set_ticklabels([])
        ax.yaxis.set_ticklabels([])
        ax.zaxis.set_ticklabels([])
        ax.view_init(30, angle)

        return self.get_image(ax)

    def get_p1(self):
        return 1.0

    def get_p2(self):
        return 0.5

    def get_s(self, p1, p2):
        return "??"

    def get_v(self, p1, p2):
        return "??"
