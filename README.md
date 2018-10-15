# PySide2-Designer

Qt for Python is great, but not as easy to use initaly as C++ and QtCreator, on Python you cannot use .ui files directly from your program without a little work.

I have found two methods of achiving thisfrom Python:

1. Google pyside_dynamic.py (https://gist.github.com/cpbotha) and use this to dynamicaly access your ui files

2. use pyside2-uic for ui files, and pyside2-rcc for resources.
