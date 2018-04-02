
import wx

class Frame(wx.Frame):
    
    def __init__(self, parent=None, id=-1,
                pos=wx.DefaultPosition,
                title="BookCase Manager"):
        wx.Frame.__init__(self, parent, id, title, pos, size=(1100, 650))


class App(wx.App):
    
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

def main():
    app = App()
    app.MainLoop()

if __name__ == '__main__':
    main()