from gui.frames import MainFrame
from gui.main_app import PyExportDB


def main():
    app = PyExportDB()
    frame = MainFrame(None)

    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
