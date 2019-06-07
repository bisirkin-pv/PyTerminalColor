# PyTerminalColor
Coloring text in the terminal

## Get started

Add a files to your project
```bash
git clone https://github.com/bisirkin-pv/PyTerminalColor.git
```

Import a module from your project
```python
from PyTerminalColor import PyTerminalColor
```

Initialize the object by specifying the path to the configuration file 
(by default, the file is located in the same directory as the module).
```python
pyTerminalColor = PyTerminalColor('config.json')
```

To color the text, call function `colorize` by passing the necessary color parameters. 

Example:
```python
print(pyTerminalColor.colorize('Text', "yellow", "lightGray", "underline"))
```