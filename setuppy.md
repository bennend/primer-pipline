## The setup file for cx_Freeze which is used to transform the Python code of the pipeline in to executable software.
```
import sys
# sys.path.append('/Users/tongbangzhuo/Documents/cx_Freeze-5.0.2/build/lib.macosx-10.13-intel-2.7')
import os
# os.environ['TCL_LIBRARY']='/Library/Frameworks/Tcl.framework/Versions/8.6/Tcl'
from cx_Freeze import setup, Executable


base = None
if sys.platform == 'win32':
      base='Win32GUI'

executables=[Executable('/Users/tongbangzhuo/PycharmProjects/projectfiles/GUI.py',base=base)]


options={
      'build_exe':{
            'excludes':['tcl'],
            'packages':['os','tkinter','Bio.Align','Bio','subprocess','numpy','matplotlib','xlsxwriter']
      }
}

setup(name='Doughnut',
      version='beta',
      description='Primer designing pipline',
      options=options,
      executables=executables)

```
