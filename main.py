
import os
import sys
import logging

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot
from PySide2.QtGui import QIcon

# Create python source from the Ui file and resource from .qrc.
os.system("pyside2-uic main.ui > main_ui.py")
os.system("pyside2-rcc res.qrc -o res_qrc.py")

# Import the newly updated resources.
from ui.main_ui import Ui_MainWindow
from ui.res_qrc import qInitResources

# ------------------------------------------------------------
# ------------------------------------------------------------
class MainWindow(QMainWindow, Ui_MainWindow):

    # ------------------------------------------------------------
    # ------------------------------------------------------------
    def __init__(self, parent=None):

        super().__init__(parent)

        #
        self.setupUi(self)

        # Set the window title.
        self.setWindowTitle('Example')

    @Slot(int)
    def on_button_clicked(self):
        logging.debug("push button clicked!")

# ------------------------------------------------------------
# ------------------------------------------------------------
def main():

    # output debug messages.
    logging.basicConfig(level=logging.DEBUG)

    app = QApplication(sys.argv)

    # Create an instance of MainWindow
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())


# ------------------------------------------------------------
# ------------------------------------------------------------
if __name__ == '__main__':

    main()
