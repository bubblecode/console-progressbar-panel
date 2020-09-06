# console-progressbar-panel
![PyPI](https://img.shields.io/pypi/v/consoleProgressbarPanel)
![PyPI - License](https://img.shields.io/pypi/l/consoleProgressbarPanel?style=plastic)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/bubblecode/console-progressbar-panel)
![GitHub last commit](https://img.shields.io/github/last-commit/bubblecode/console-progressbar-panel)

A simple Python console progress bar
### install
```shell
$ pip install consoleProgressbarPanel
```
### class ProgressBar(name, total_length, inner_width=29, moniter=[], **kwargs)
 - **name**: The name of the progress bar panel (e.g 'New Task')
 - **total_length**: Maximum iteration value (e.g 10)
 - **inner_width**: The width of the panel (e.g 30)
 - **moniter**: Variable name monitored during progress bar (e.g ['var1', 'var2'])
 - **\*\*kwargs**: Static variable information displayed on the progress bar (e.g param1=0.3)
> **update(i, \*\*monite)**<br>
> **i**: Current progress bar value (1<= i <= total_length)<br>
> **monite**: Parameter that need to be monitored (indicated in moniter)
### example
```python
import time
from consoleProgressbarPanel import consoleProgressbarPanel
pb = consoleProgressbarPanel.ProgressBar(
                 name='Model',
                 total_length=10, 
                 inner_width=30, 
                 moniter=['mma','mmb'], 
                 parama= 0.3, 
                 paramb='xxx')
a = [0.1,0.3,0.2,0.4,0.5,0.7,0.2,0.1,0.0,0.3]
b = [1.0,-1.0,1.0,3.0,6.0,8.0,4.0,3.0,2.0,1.0]
for i in range(1, len(pb)):
    pb.update(i, mma=a[i-1],mmb=b[i-1])
    time.sleep(1) # we use this function in order to see more clearly. 
```
```shell
.____________________________.
| name      Model            |
|---------parameter----------|
| parama: 0.3                |
| paramb: xxx                |
|                            |
|----------moniter-----------|
| mma 0.1                    |
| mmb 3.0                    |
|____________________________|
|[================----] 8/10 |
|____________________________|
```

## In addition, we encapsulated the panels that make up the progress bar into components
------
You can use these components to customize your own panels.
### COM_HEADER_LINE(inner_width: int)
> This component is usually used to form the head of the console panel.
```python
com_header = consoleProgressbarPanel.COM_HEADER_LINE(30)
print(com_header)
```
```shell
.______________________________.
```
### COM_MARK_SPLIT(inner_width: int, mark=' ')
> This component is usually used to fill the console panel.
 - you can create a blank area
```python
com_blank = consoleProgressbarPanel.COM_MARK_SPLIT(25)
```
```shell
|                         |
```
 - or you can also provide a 'mark'
```python
com_marksp = consoleProgressbarPanel.COM_MARK_SPLIT(25, '*')
print(com_marksp)
```
```shell
|*************************|
```
### COM_MODULE_SPLIT_LINE(inner_width: int, name: str)
> This component is usually used to divide the panel into many different modules.
```python
com_split = consoleProgressbarPanel.COM_MODULE_SPLIT_LINE(25, 'split')
print(com_split)
```
```shell
|----------split----------|
```
### COM_STATIC_INFO(inner_width: int, key: str, value: any)
> You can use this component to display some constant information (such as model hyperparameters).
```python
com_info = consoleProgressbarPanel.COM_STATIC_INFO(25, 'param1', '1.414')
print(com_info)
```
```shell
| param1 1.414            |
```
### COM_INFORMATION(inner_width: int)
> You can use this component to display some information that changes in real time as the progress bar changes.
```python
com_monite = consoleProgressbarPanel.COM_INFORMATION(25)
print(com_monite.update('param2', 85))
```
```shell
| param2 85               |
```
