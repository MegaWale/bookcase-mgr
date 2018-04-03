import wx
from wx.py.shell import ShellFrame
from wx.py.filling import FillingFrame



class ToolbarFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "TOOL BARZZZ",
                    size=(500, 300))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        statusBar = self.CreateStatusBar()
        toolbar = self.CreateToolBar()
        # toolbar.AddSimpleTool(wx.NewId(), images.getNewBitmap(),
        #                         "New", "Long help for 'New'")
        toolbar.Realize()
        menubar = wx.MenuBar()
        menu1 = wx.Menu()
        menubar.Append(menu1, "&File")
        menu2 = wx.Menu()

        menu2.Append(wx.NewId(), "&Copy", "Copy in status bar")
        menu2.Append(wx.NewId(), "C&ut", "")
        menu2.Append(wx.NewId(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "&Options...", "Display options")
        menubar.Append(menu2, "&Edit")

        menu3 = wx.Menu()
        shell = menu3.Append(-1, "&wxPython shell", "Open wxPython shell frame")
        filling = menu3.Append(-1, "&Namespace viewer", "Open namespaces viewer frame")
        menubar.Append(menu3, "&Debug!!!")
        self.Bind(wx.EVT_MENU, self.OnShell, shell)
        self.Bind(wx.EVT_MENU, self.OnFilling, filling)

        self.SetMenuBar(menubar)

    def OnCloseMe(self, event):
        self.Close(True)

    def OnCloseWindow(self, event):
        self.Destroy()

    def OnShell(self, event):
        frame = ShellFrame(parent=self)
        frame.Show()

    def OnFilling(self, event):
        frame = FillingFrame(parent=self)
        frame.Show()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()