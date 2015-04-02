import wx

# #######################################################################
class TestPopup(wx.PopupWindow):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent, style):
        """Constructor"""
        wx.PopupWindow.__init__(self, parent, style)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        st = wx.StaticText(self, -1,
                           "This is a special kind of top level\n"
                           "window that can be used for\n"
                           "popup menus, combobox popups\n"
                           "and such.\n\n")
        sizer.AddF(st, wx.SizerFlags().Expand().Border(wx.ALL, 8))

        btn_close = wx.Button(self, -1, "Close")
        self.Bind(wx.EVT_BUTTON, self._on_close_popup, btn_close)
        sizer.AddF(btn_close, wx.SizerFlags().Right().Border(wx.ALL, 8))

        self.Fit()
        wx.CallAfter(self.Refresh)

    def _on_close_popup(self, event):
        self.Show(False)
        self.Destroy()


class TestPanel(wx.Panel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent)

        btn = wx.Button(self, label="Open Popup")
        btn.Bind(wx.EVT_BUTTON, self.onShowPopup)


    #----------------------------------------------------------------------
    def onShowPopup(self, event):
        """"""
        win = TestPopup(self.GetTopLevelParent(), wx.SIMPLE_BORDER)

        # btn = event.GetEventObject()
        # pos = btn.ClientToScreen((0, 0))
        # sz = btn.GetSize()
        # win.Position(pos, (0, sz[1]))

        dw, dh = wx.DisplaySize()
        w, h = win.GetSize()
        x = dw - w - 5
        y = dh - h - 30
        win.SetPosition((x, y))

        win.Show(True)


# #######################################################################
class TestFrame(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, title="Test Popup")
        self.panel = TestPanel(self)

        self.task_bar_icon = wx.TaskBarIcon(iconType=wx.TBI_DEFAULT_TYPE)
        self.task_bar_icon.SetIcon(wx.ArtProvider.GetIcon(wx.ART_GO_HOME))

        self.task_bar_icon.Bind(wx.EVT_TASKBAR_LEFT_DOWN, self._on_left_down)
        self.Show()

    def _on_left_down(self, event):
        self.panel.onShowPopup(event)

#----------------------------------------------------------------------
if __name__ == "__main__":
    app = wx.App(False)

    frame = TestFrame()
    app.MainLoop()