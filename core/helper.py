import numpy as np
from PIL import Image, ImageTk


def get_z(z, x, y):
    return np.array([[z]*len(x), [z]*len(y)])


def convert_to_tk_image(cv2_img):
    img = Image.fromarray(cv2_img)
    # return img
    return ImageTk.PhotoImage(img)
