import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
from PIL import Image

from .helper import get_z, convert_to_tk_image


class Figure:

    def __init__(self, name):
        self.__name = name
        self.chess_shape = (5, 4)

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

        plt.close(figure)

        img = Image.open(figure_data)
        return np.array(img)
        # return ImageTk.PhotoImage(img)

    def make_figure(self):
        return self.ax

    def figure_image3d(self, angle):
        ax = self.make_figure()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.xaxis.set_ticklabels([])
        ax.yaxis.set_ticklabels([])
        ax.zaxis.set_ticklabels([])
        ax.view_init(30, angle)

        return self.get_image(ax)

    def image3d(self, img, angle):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, self.chess_shape, None)
        if not ret:
            return convert_to_tk_image(img)

        surface = np.float32([corners[0, 0], corners[self.chess_shape[0] - 1, 0],
                              corners[len(corners) - 1, 0], corners[len(corners) - self.chess_shape[0], 0]])

        aug_img = self.figure_image3d(angle)
        h, w, ch = aug_img.shape
        aug_surface = np.float32([[0, 0], [w, 0], [w, h], [0, h]])

        h, w, ch = img.shape
        perspective = cv2.getPerspectiveTransform(aug_surface, surface)

        dst = cv2.warpPerspective(aug_img, perspective, (w, h))
        mask_threshold = 10
        ret, mask = cv2.threshold(cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY), mask_threshold, 1, cv2.THRESH_BINARY_INV)
        # Erode and dilate are used to delete the noise
        mask = cv2.erode(mask, (3, 3))
        mask = cv2.dilate(mask, (3, 3))
        # The two images are added using the mask
        for c in range(0, ch):
            img[:, :, c] = dst[:, :, c] * (1 - mask[:, :]) + img[:, :, c] * mask[:, :]
        return convert_to_tk_image(img)

    def get_p1(self):
        return 1.0

    def get_p2(self):
        return 0.5

    def get_p3(self):
        return 0.2

    def get_s(self, p1, p2, p3):
        return "??"

    def get_v(self, p1, p2, p3):
        return "??"

    @property
    def has_p1(self):
        return True

    @property
    def has_p2(self):
        return False

    @property
    def has_p3(self):
        return False
