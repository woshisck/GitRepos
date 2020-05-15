import unreal

from PySide import QtGui, QtUiTools, QtCore

from PySide.QtGui import QMessageBox
from PySide.QtGui import QFileDialog

workingPath = "/Game/"

@unreal.uclass()


def work_for_all(func):
    def inner_func(*args, **kwargs):
        print("I cam work for all function?")
        return func(*args, **kwargs)
    return inner_func

def T_Param(func):
    def inner_func(A,B):
        if (A <=0):
            print ("A is lower than zero")
        return func(A,B)
    return inner_func

def T_Param_(func):
    def inner_func(A,B):
        if(B==5):
            print ("B is 5")
        return func(A,B)
    return inner_func



@T_Param
@T_Param_
def DIVID(A,B):
    return A/B

@work_for_all
def divide(a,b):
    return a+b

print divide(3,4)

def fun_func(*args):
    return args




print( DIVID(0,5))