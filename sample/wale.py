import wx


class wale(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300, 200))


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = wale(parent=None,id=-1)
    frame.show()
    app.MainLoop()