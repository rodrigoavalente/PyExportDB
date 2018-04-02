from gui.main_app import PyExportDB
from gui.frames.main_frame import MainFrame

def main():    
    app = PyExportDB()
    frame = MainFrame(None, title="PyExportDB")

    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
