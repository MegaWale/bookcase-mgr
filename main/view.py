
import wx

class Frame(wx.Frame):
    
    def __init__(self, parent=None, id=-1,
                pos=wx.DefaultPosition,
                title="BookCase Manager"):
        wx.Frame.__init__(self, parent, id, title, pos, size=(1100, 650))
        panel = wx.Panel(self)

        # Creating a status bar
        status = self.CreateStatusBar()

        # Creating a menu bar
        menubar = wx.MenuBar()
        first = wx.Menu()
        second = wx.Menu()

        first.Append(wx.NewId(), "New window", "This a New Window")
        first.Append(wx.NewId(), "Open ...", "This a open wlnlksfjdk Window")

        menubar.Append(first, "File")
        menubar.Append(second, "Edit")
        self.SetMenuBar(menubar)


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