<h1 align="center" id="title">DashBoard using PyQt5</h1>

<p align="center"><img src="https://socialify.git.ci/MBMishu/DashBoard-PyQt5/image?font=KoHo&amp;language=1&amp;name=1&amp;owner=1&amp;pattern=Circuit%20Board&amp;theme=Dark" alt="project-image"></p>

<h2>🚀 Demo</h2>

[https://github.com/MBMishu/DashBoard-PyQt5/blob/main/image.png](https://github.com/MBMishu/DashBoard-PyQt5/blob/main/image.png)

<h2>Project Screenshots:</h2>

<img src="https://github.com/MBMishu/DashBoard-PyQt5/blob/main/image.png" alt="project-screenshot" width="400" height="400/">

<h2>🛠️ Installation Steps:</h2>

<p>1. Qt Designer is available on PyPi via the pyqt5-tools package</p>

```
pip install pyqt5-tools
```

<p>2. After installation you can run Qt Designer from the command line using the built-in launcher.</p>

```
pyqt5-tools designer
```

<p>3. Install PySide2</p>

```
pip install PySide2
```

<p>4. Convert .ui file to .py: Use pyside2-uic to convert your .ui file to a Python file:</p>

```
pyside6-uic interface.ui -o ui_interface.py
```

<p>5. Convert .qrc file to .py: If you have a resource file (.qrc) convert it using pyside2-rcc</p>

```
pyside6-rcc resources.qrc -o resources_rc.py
```

<p>6. main.py</p>

```
import sys from PySide2.QtWidgets import QApplication QMainWindow from ui_interface import Ui_MainWindow  class MainWindow(QMainWindow):     def __init__(self):         super(MainWindow self).__init__()         self.ui = Ui_MainWindow()         self.ui.setupUi(self)  if __name__ == "__main__":     app = QApplication(sys.argv)     window = MainWindow()     window.show()     sys.exit(app.exec_())
```

<p>7. custom widgets</p>

```
pip install QT-PyQt-PySide-Custom-Widgets
```

<p>8. pip install PySide6</p>

```
pip install PySide6
```

```
pyinstaller test.py --icon favicon.ico --exclude PySide2 --exclude PyQt5 --exclude PyQt6
```

if you are using pyfiglet then

```
pyinstaller test.py --icon favicon.ico --exclude PySide2 --exclude PyQt5 --exclude PyQt6 --add-data "<path-to-pyfiglet>/fonts:pyfiglet/fonts"
```

```
pyinstaller main_2.py --icon favicon.ico --exclude PySide2 --exclude PyQt5 --exclude PyQt6 --add-data "c:\users\user\.conda\envs\dubotech\lib\site-packages/pyfiglet/fonts:pyfiglet/fonts" --add-data "google_map.html;." --add-data "octopus_mini_svg.svg;."
```
