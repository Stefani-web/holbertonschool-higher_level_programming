<p align="center"><img src="https://cdn.discordapp.com/attachments/1217825406699180052/1243860284162969650/Python_abc.jpg?ex=665302a9&is=6651b129&hm=adebf666390d6ad583dfc85362d840efa7acf0ad6c987fe09452565805ba3098&"  alt="Python"/> </p>

<p>

**Abstract Classes:**
An abstract class is used to define a common interface for multiple component implementations.
It can contain abstract methods, that is to say methods without a concrete implementation.
Abstract classes serve as templates for other classes that inherit from them.
In Python, we use the abc (Abstract Base Classes) module to create abstract classes.

**Here is an example of an abstract class with abstract methods:**

```
from abc import ABC, abstractmethod

class Animal(ABC):
     @abstractmethod
     def move(self):
         pass

class Human(Animal):
     def move(self):
         print("I can walk and run")

class Snake(Animal):
     def move(self):
         print("I can crawl")

class Dog(Animal):
     def move(self):
         print("I can bark")

class Lion(Animal):
     def move(self):
         print("I can roar")

# Example of use
R = Human()
R.move() # Shows "I can walk and run"
```
**Interfaces:**
An interface in Python is a set of method signatures that classes implementing that interface must provide.
Unlike abstract classes, interfaces only contain methods without implementation.
In Python you can simulate interfaces using abstract classes with only abstract methods.

**Here is an example of an interface declaration in Python:**
```
import zope.interface

class MyInterface(zope.interface.Interface):
    x = zope.interface.Attribute("foo")

    def method1(self, x):
        pass

    def method2(self):
        pass

# Exemple d'utilisation
x = MyInterface['x']
print(x)  # Affiche l'attribut 'x' de l'interface
```

</p>

<p align="center">
<img src="https://cdn-images.threadless.com/threadless-media/artist_shops/shops/realpython/profile/logo-1613591159-afae41b42c1708f4675432b0af9e0f8e.png?v=3&d=eyJvcHMiOiBbWyJyZXNpemUiLCBbMzUwXSwge31dXSwgImZvcmNlIjogZmFsc2UsICJvbmx5X21ldGEiOiBmYWxzZX0=" alt="Python"/>
</p>

## ➤ INSTALLATION INSTRUCTIONS

```
Python Scripts:
- Allowed editors: vi, vim, emacs
- Python scripts must be written to run with Python 3.8.5 on Ubuntu 20.04 LTS, using python3 (version 3.8.*)
- Files must end with a new line and the first line must be exactly #!/usr/bin/python3.
- The code must follow the PEP 8 style (pycodestyle version 2.7.*).
- All files must be executable and file length will be tested with wc.

```

## ➤ TUTORIALS

- [Python 3 Object-Oriented Programming](https://docs.python.org/3/tutorial/classes.html)
- [ABC — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Real Python - Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Corey Schafer - OOP Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
- [sentdex - Python OOP Tutorial](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfhTF3Zfyzc_yD-Mq9iTp4G)

## ➤ LICENSE

Distributed under the MIT License. See [LICENSE](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-abc/LICENSE) for more information.

Copyright (c) 2024 Stephanie CARVALHO

## ➤ [AUTHORS](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/AUTHORS)

* [Stephanie Carvalho](https://github.com/Stefani-web)
