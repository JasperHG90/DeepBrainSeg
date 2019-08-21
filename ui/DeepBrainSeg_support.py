#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.25
#  in conjunction with Tcl version 8.6
#    Aug 21, 2019 09:22:40 AM IST  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global progress_bar
    progress_bar = tk.IntVar()

def Get_Segmentation():
    print('DeepBrainSeg_support.Get_Segmentation')
    sys.stdout.flush()

def Load_Flair():
    print('DeepBrainSeg_support.Load_Flair')
    sys.stdout.flush()

def Load_T1():
    print('DeepBrainSeg_support.Load_T1')
    sys.stdout.flush()

def Load_T1ce():
    print('DeepBrainSeg_support.Load_T1ce')
    sys.stdout.flush()

def Load_T2():
    print('DeepBrainSeg_support.Load_T2')
    sys.stdout.flush()

def SegmentationOverlay():
    print('DeepBrainSeg_support.SegmentationOverlay')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import DeepBrainSeg
    DeepBrainSeg.vp_start_gui()




