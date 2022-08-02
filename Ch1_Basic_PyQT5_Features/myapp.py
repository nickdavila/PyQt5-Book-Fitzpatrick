# Notes
# Qt is a toolkit for creating cross-platform GUI applications, PyQT is a wrapper for the C++ Qt library to allow it to be used in Python

from PyQt5.QtWidgets import QApplication, QWidget

#Only needed for access to command line arguments
import sys


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplications([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()   # IMPORTANT!!! Windows are hidden by default. .show() makes it visible

# Start the event loop.
app.exec_()


# Application won't reach here until you exit and the event loop has stopped.