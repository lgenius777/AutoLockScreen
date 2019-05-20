from ctypes import *
user32=windll.LoadLibrary('user32.dll')
def lockScreen():
    user32.LockWorkStation()
