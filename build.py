from qtpy import uic
import os

# cpp files in python compilieren (liegen im ui ordner)
uic.compileUiDir(os.path.dirname(os.path.abspath(__file__))+"/ui")
