#!/usr/bin/env python
# coding=utf-8

# import wx
#
# from settings import Settings
# from button import Button
# import game_functions as gf
#
#
# class Display_windows(wx.App):
#     FLTL_settings = Settings()
#
#     def OnInit(self):
#         frame = wx.Frame(parent=None, title="FLTL", size=(self.FLTL_settings.screen_height, self.FLTL_settings.screen_width))
#         frame.Show()
#         return True


import wx

class Frame(wx.Frame):
    """Frame class that displays an image."""

    def __init__(self, image, parent=None, id=-1,
            pos = wx.DefaultPosition,
            title = 'FLTL'):

        """Create a Frame instance and display image."""
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)


class App(wx.App):
    """Application class."""

    def OnInit(self):
        image = wx.Image('wxPython.jpg', wx.BITMAP_TYPE_JPEG)
        self.frame = Frame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


def main():
    app = App()
    app.MainLoop()

if __name__ == '__main__':
    app = App()
    app.MainLoop()
