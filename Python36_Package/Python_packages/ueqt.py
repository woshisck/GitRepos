import sys
import unreal_engine as ue
import PySide2
from PySide2 import QtWidgets

app = QtWidgets.QApplication(sys.argv)

def ticker_loop(delta_time):
    app.processEvents()
    return True

ticker = ue.add_ticker(ticker_loop)