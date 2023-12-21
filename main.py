from ContentWindow import ContentWindow
from ControlWindow import ControlWindow
from Controller import Controller

if __name__ == "__main__":
    content_window = ContentWindow()
    controller = Controller(content_window)
    control_window = ControlWindow(controller)
    control_window.start()
    content_window.start()
