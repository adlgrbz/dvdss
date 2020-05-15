#!/usr/bin/python3

from random import randint
from os import path, getenv
from tkinter import Tk, Canvas, PhotoImage
from signal import signal, SIGINT, SIG_DFL, SIGTERM


this_dir, this_filename = path.split(__file__)


def determine_window_id(win_id=None):
    if not win_id:
        win_id = getenv("XSCREENSAVER_WINDOW")

    if win_id:
        win_id = int(win_id, 16)

    return win_id


class SS(Tk):
    def __init__(self):
        super().__init__()
        # self.lift()
        # self.attributes("-fullscreen", True)
        # self.attributes('-topmost', True)

        self.sw = 700  # self.winfo_screenwidth()
        self.sh = 500  # self.winfo_screenheight()

        self.x = self.sw / 2
        self.y = self.sh / 2
        self.vx = randint(-3, 3)
        self.vy = randint(-3, 3)
        self.img_index = 0

        self.c = Canvas(width=self.sw, height=self.sh)
        self.c.config(bg="black", bd=0, highlightthickness=0)
        self.c.pack()

        dvd_img = PhotoImage(file=f"{this_dir}/data/{self.img_index}.gif")
        self.dvd = dvd_img

        self.dvd_w = self.dvd.width() / 2
        self.dvd_h = self.dvd.height() / 2

        self.img = self.c.create_image(self.x, self.y, image=dvd_img)

        self.main()

    def change_img(self):
        self.img_index += 1
        self.dvd["file"] = f"{this_dir}/data/{self.img_index}.gif"

    def main(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        if self.x - self.dvd_w < 0 or self.x + self.dvd_w > self.sw:
            self.vx = -self.vx
            self.change_img()

        if self.y - self.dvd_h < 0 or self.y + self.dvd_h > self.sh:
            self.vy = -self.vy
            self.change_img()

        if self.img_index >= 6:
            self.img_index = 0

        self.c.coords(self.img, self.x, self.y)
        self.c.after(20, self.main)


def main():
    ss = SS()

    signal(SIGINT, SIG_DFL)
    signal(SIGTERM, lambda: ss.destroy())

    ss.mainloop()
