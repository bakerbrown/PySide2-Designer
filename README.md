# PySide2-Designer

Qt for Python is great, but not as easy to use initially as C++ and Qt Creator, on Python you cannot use .ui files directly from your program without a little work.

I have found two methods of achieving this from Python:

1. Google pyside_dynamic.py (https://gist.github.com/cpbotha) and use this to dynamically access your ui files

2. convert the ui and resource files a runtime by using pyside2-uic for ui files, and pyside2-rcc for resources respectively.

