import wx
import gui as wxFormBuilderTest

import ImagesToPDF as convert

class TransformFrame(wxFormBuilderTest.MainFrame):
    def __init__(self, parent):
        wxFormBuilderTest.MainFrame.__init__(self, None)
    
    def TransformFile(self, event):
        location = self.DirPicker.GetPath()
        self.m_staticText3.SetLabel(u"Processing files...")
        self.m_staticText3.Update()
        self.Update()
        convert.process(location)


if __name__ == "__main__":
    app = wx.App(False)
    frame = TransformFrame(None)
    frame.Show(True)
    app.MainLoop()
