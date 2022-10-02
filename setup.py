import sys
from cx_Freeze import Executable, setup, executable

build_exe_options = {'packages': ['os'], 'includes': ['tkinter']}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'
    
setup(
    nome = 'calculadora',
    version = '0.1',
    description = 'Calculadora',
    options = {'build_exe': build_exe_options},
    executables = {Executable('calculator.py', base=base)}
)