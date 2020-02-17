import tkinter as tk
from functools import partial

import sched
import time

from .cube import Cube
from .ball import Ball
from .pyramid import Pyramid
from .cylinder import Cylinder
from .cone import Cone
from .conoid import Conoid

import warnings
warnings.simplefilter("ignore", UserWarning)

W = 380
H = 640


class App:
    canvas = None
    selected_figure = None
    tk_image = None
    param_frame = None

    def __init__(self, window):
        self.s = sched.scheduler(time.time, time.sleep)

        self.window = window
        self.window.wm_title("3D models")
        self.window.geometry("{}x{}+200+10".format(W, H))

        self.figure_title_str = tk.StringVar()
        self.figure_title_str.set("Figure: -----")

        self.figure_p1 = tk.StringVar()
        self.figure_p1.set("1.0")

        self.figure_p2 = tk.StringVar()
        self.figure_p2.set("0.5")

        self.figure_p3 = tk.StringVar()
        self.figure_p3.set("0.2")

        self.figure_s = tk.StringVar()
        self.figure_s.set("??")

        self.figure_v = tk.StringVar()
        self.figure_v.set("??")

        self.figure_p1.trace("w", self.update_p)
        self.figure_p2.trace("w", self.update_p)

        self.figures = [Cube(), Ball(), Pyramid(), Cylinder(), Cone(), Conoid()]

        self.frame_home = tk.Frame(bg="gray", bd=1, width=W, height=H)
        self.frame_figure = tk.Frame(bg="gray", bd=1, width=W, height=H)
        self.fill_frame_home(self.frame_home)
        self.fill_frame_figure(self.frame_figure)

        self.frame_home.place(x=0, y=0)

        self.angle = -20
        self.stop = False

    def fill_frame_home(self, parent):
        title = tk.Label(parent, width=17, height=2, text="Select 3D figure",
                         font=("Helvetica", 24), fg="gold2")
        title.place(x=0, y=0)

        buttons = [tk.Button(parent, text=figure.name,
                             font=("Helvetica", 16),
                             width=8, height=3, bg="green2",
                             command=partial(self.show_figure, figure)) for figure in self.figures]
        for i, button in enumerate(buttons):
            x = 40 + (i // 3) * 170
            y = 110 + (i % 3) * 140
            button.place(x=x, y=y)

        btn_exit = tk.Button(parent, text="Exit",
                             font=("Helvetica", 16),
                             width=19, height=2, bg="red2",
                             command=self.quit)
        btn_exit.place(x=38, y=540)

    def fill_frame_figure(self, parent):
        figure_title = tk.Label(parent, width=24, height=1, textvariable=self.figure_title_str,
                                font=("Helvetica", 16), fg="gold2")
        figure_title.place(x=0, y=0)

        self.canvas = tk.Canvas(parent, width=W, height=H-290, bg="white")
        self.canvas.place(x=0, y=40)

        self.param_frame = None
        btn_return = tk.Button(parent, text="Return back",
                               font=("Helvetica", 12),
                               width=26, height=1, bg="green2",
                               command=self.show_home)
        btn_return.place(x=38, y=570)

    def update_p(self, name, index, mode):
        p1 = self.figure_p1.get()
        p2 = self.figure_p2.get()
        p3 = self.figure_p3.get()
        s = self.selected_figure.get_s(p1, p2, p3)
        self.figure_s.set(s)

        v = self.selected_figure.get_v(p1, p2, p3)
        self.figure_v.set(v)

    def fill_frame_params(self, parent):
        # param 1
        y = 5
        x = 6
        label = tk.Label(parent, width=4, height=1, text="R=",
                         font=("Helvetica", 12), fg="black")
        label.place(x=x, y=y)

        entry = tk.Entry(parent, width=8, textvariable=self.figure_p1)
        entry.place(x=x+40, y=y+3)

        # param 2
        if self.selected_figure.has_p2:
            y += 29
            label2 = tk.Label(parent, width=4, height=1, text="H=",
                              font=("Helvetica", 12), fg="black")
            label2.place(x=x, y=y)

            entry2 = tk.Entry(parent, width=8, textvariable=self.figure_p2)
            entry2.place(x=x+40, y=y+3)

            # param 3
            if self.selected_figure.has_p3:
                y += 29
                label3 = tk.Label(parent, width=4, height=1, text="h=",
                                  font=("Helvetica", 12), fg="black")
                label3.place(x=x, y=y)

                entry3 = tk.Entry(parent, width=8, textvariable=self.figure_p3)
                entry3.place(x=x + 40, y=y + 3)

        # S
        y = 5
        x = 200
        label = tk.Label(parent, width=4, height=1, text="S=",
                         font=("Helvetica", 12), fg="black")
        label.place(x=x, y=y)

        entry = tk.Entry(parent, width=8, textvariable=self.figure_s, state=tk.DISABLED)
        entry.place(x=x+40, y=y+3)

        # Volume
        y += 29
        label = tk.Label(parent, width=4, height=1, text="V=",
                         font=("Helvetica", 12), fg="black")
        label.place(x=x, y=y)

        entry = tk.Entry(parent, width=8, textvariable=self.figure_v, state=tk.DISABLED)
        entry.place(x=x+40, y=y+3)

    def show_figure(self, figure):
        self.selected_figure = figure
        self.figure_title_str.set("Figure: {}".format(figure.name))

        if self.param_frame is not None:
            self.param_frame.destroy()
            self.param_frame = None

        self.param_frame = tk.LabelFrame(self.frame_figure, width=W, height=140)
        self.param_frame.place(x=0, y=H-240)
        self.fill_frame_params(self.param_frame)

        self.frame_home.pack_forget()
        self.frame_figure.pack()

        self.figure_p1.set(str(self.selected_figure.get_p1()))
        self.figure_p2.set(str(self.selected_figure.get_p2()))
        self.figure_p3.set(str(self.selected_figure.get_p3()))

        self.angle = -20
        self.update_figure()

    def update_figure(self):
        self.tk_image = self.selected_figure.image3d(self.angle)
        self.canvas.delete("figure")
        self.canvas.create_image(-40, 0, image=self.tk_image, tag="figure", anchor=tk.NW)

    def show_home(self):
        self.selected_figure = None
        self.frame_figure.pack_forget()
        self.frame_home.pack()

    def update(self):
        if self.stop:
            return
        if self.selected_figure is not None:
            self.angle += 10
            self.update_figure()

        self.window.update()
        self.s.enter(0.2, 1, self.update)

    def quit(self):
        self.stop = True
        self.window.quit()

    def run(self):
        self.window.protocol("WM_DELETE_WINDOW", self.quit)
        self.s.enter(0.2, 1, self.update)
        self.s.run()
        # self.window.mainloop()
