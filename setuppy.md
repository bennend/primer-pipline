## The setup file for cx_Freeze which is used to transform the Python code of the pipeline in to executable software.
```
import sys
import os
from cx_Freeze import setup, Executable


base = None
if sys.platform == 'win32':
      base='Win32GUI'

executables=[Executable('the path of the python script',base=base)]


options={
      'build_exe':{
            'excludes':['tcl'],
            'packages':['os','tkinter','Bio.Align','Bio','subprocess','numpy','matplotlib','xlsxwriter']
      }
}

setup(name='PrimerDesigner',
      version='beta',
      description='Primer designing pipline',
      options=options,
      executables=executables)

```
