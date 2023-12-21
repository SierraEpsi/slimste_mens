from ContentWindow import ContentWindow
from ControlWindow import ControlWindow
from Controller import Controller

if __name__ == "__main__":
    content_window = ContentWindow()
    control_window = ControlWindow()
    controller = Controller(content_window, control_window)
    control_window.set_controller(controller)

    control_window.start()
    content_window.start()
