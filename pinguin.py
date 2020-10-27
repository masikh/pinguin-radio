#!/usr/bin/env python3
from InternetRadio import Stations
from math import sqrt, ceil
from PIL import Image, ImageTk
from functools import partial
import subprocess
import tkinter


class FFMpeg:
    def __init__(self):
        self.process = None
        self.binary = '/usr/bin/ffplay'

    def play(self, url):
        if self.process is not None:
            self.process.kill()

        with open(os.devnull, 'w') as fh:
            cmd = [self.binary, '-nodisp', url]
            self.process = subprocess.Popen(cmd, stdout=fh, stderr=fh)


class UI:
    def __init__(self, root_dir):
        self.stations = Stations().data
        self.logo_dir = '{root_dir}/logos'.format(root_dir=root_dir)
        self.player = FFMpeg()

    def play(self, url):
        self.player.play(url)

    def run(self):
        # Create & Configure root
        root = tkinter.Tk()
        root.title('Pinguin Radio')

        tkinter.Grid.rowconfigure(root, 0, weight=1)
        tkinter.Grid.columnconfigure(root, 0, weight=1)

        # Create & Configure frame
        frame = tkinter.Frame(root)
        frame.grid(row=0, column=0, sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)

        rows = ceil(sqrt(len(self.stations)))
        cols = ceil(len(self.stations) / rows)

        keys = [x for x in self.stations.keys()]

        # Create a N x ~N grid
        count = 0
        for row_index in range(rows):
            tkinter.Grid.rowconfigure(frame, row_index, weight=1)
            for col_index in range(cols):
                if count > len(self.stations) - 1:
                    continue
                key = keys[count]
                tkinter.Grid.columnconfigure(frame, col_index, weight=1)
                logo = Image.open('{path}/{logo}'.format(path=self.logo_dir, logo=self.stations[key]['logo']))
                logo = logo.resize((75, 75), Image.ANTIALIAS)
                self.stations[key]['image'] = ImageTk.PhotoImage(logo)
                self.stations[key]['button'] = tkinter.Button(frame, text=key, image=self.stations[key]['image'], border=1, compound="bottom")
                self.stations[key]['button'].grid(row=row_index, column=col_index, sticky=tkinter.N + tkinter.S + tkinter.E + tkinter.W)
                self.stations[key]['button'].configure(command=partial(self.play, self.stations[key]['url']))
                self.stations[key]['button'].configure(width=90)
                self.stations[key]['button'].configure(height=90)
                self.stations[key]['button'].configure(text=key)
                count += 1
        root.mainloop()


if __name__ == '__main__':
    import os
    program_root_dir = os.path.dirname(os.path.realpath(__file__))
    ui = UI(program_root_dir)
    ui.run()
