#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# from Crawler import *
import sys
from GUI import *
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def main():
    root = Tkinter.Tk()
    app = GUI(root)
    root.geometry('640x560')
    root.resizable(False, False)
    app.master.title('网易云音乐的歌曲推荐')
    app.mainloop()



if __name__ == "__main__":
    main()
