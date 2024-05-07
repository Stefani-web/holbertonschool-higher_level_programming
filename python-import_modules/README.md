# <p align="center">python-import_modules</p>

<p align="center">
<img src="https://ioflood.com/blog/wp-content/uploads/2023/09/Importing-modules-in-Python-import-statements-module-icons-code-snippets.jpg"  alt="Python"/> </p>

<p>

The **"python-import_modules"** project aims to explore and demonstrate the different techniques for importing modules in Python. It presents methods and best practices for importing modules into a Python program, with emphasis on code modularity, readability, and maintainability</p>

<p>

**Python developers** of all levels who want to improve their understanding of importing modules in Python and learn best practices for organizing and importing modules into their projects.

The **"python-import_modules"** project aims to provide a comprehensive and accessible resource on the different techniques for importing modules in Python, as well as practical tips for effective and correct use of modules in Python projects. </p>

**Objectives:** Exploring different import methods: The project explores the different ways of importing modules in Python, including importing entire modules, specific attributes, import aliasing, etc. Using Import Directives: It covers the use of import directives such as import, from **... import**, **import ...** as, etc., and explains their advantages and limitations. Handling import paths: The project also looks at handling custom import paths using environment variables like **PYTHONPATH**, adding paths to the sys.path, or using __init__.py files. Conditional Import: It also discusses conditional import of modules based on the Python version or installed dependencies. Recommended Practices: The project highlights best practices for importing modules, including organizing modules into packages, using __all__ to control what is imported, and more.

**Expected Deliveries:**

Detailed documentation on the different methods of importing modules in **Python**.
Code samples demonstrating each import method.
Hands-on demos showing the use of import directives in real-world scenarios.
Explanations on handling custom import **paths** and conditional import.
Tips and best practices for efficient and clean module import.

<p align="center">
<img src="https://cdn-images.threadless.com/threadless-media/artist_shops/shops/realpython/profile/logo-1613591159-afae41b42c1708f4675432b0af9e0f8e.png?v=3&d=eyJvcHMiOiBbWyJyZXNpemUiLCBbMzUwXSwge31dXSwgImZvcmNlIjogZmFsc2UsICJvbmx5X21ldGEiOiBmYWxzZX0="  alt="Python"/> </p>

## ➤ INSTALLATION INSTRUCTIONS

```
Python Scripts:
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.7.*)
- The length of your files will be tested using wc

```
## ➤ EXAMPLES

1. Importing entire module:
```
import math

# Using math module functions
print(math.sqrt(25))  # Output: 5.0
```
2. Import specific attribute:
```
from math import sqrt

# Using the sqrt function directly
print(sqrt(25))  # Output: 5.0
```
3. Aliases for import:
```
import numpy as np

# Utilisation de l'alias np pour le module numpy
arr = np.array([1, 2, 3])
print(arr)  # Output: [1 2 3]
```
4. Conditional import:
```
try:
    # Python 3.x
    from urllib.request import urlopen
except ImportError:
    # Python 2.x
    from urllib import urlopen
```
5. Importing all attributes of a module:
```
from module_name import *

# Import all module attributes
# Warning: this practice is not recommended unless the module makes it explicit with __all__
```
6. Importing from a parent directory:
```
import sys
sys.path.append('../parent_directory')
from parent_module import function_name
```
7. Importing from packages:
```
from package.subpackage import module

# Using module functions or classes in the package
```
## ➤ TUTORIALS

- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command line arguments](https://docs.python.org/3/tutorial/stdlib.html#command-line-arguments)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## ➤ LICENSE

Distributed under the MIT License. See [LICENSE](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-import_modules/LICENSE) for more information.

Copyright (c) 2024 Stephanie CARVALHO

## ➤ [AUTHORS](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-import_modules/AUTHORS)

* [Stephanie Carvalho](https://github.com/Stefani-web)
