# -*- coding: utf-8 -*-
"""
 This is the main module
"""
from tkinter import Tk

from redsnapper.interface.interface import Interface

if __name__ == "__main__":
    ROOT = Tk()
    GUI = Interface(ROOT)
    ROOT.mainloop()
