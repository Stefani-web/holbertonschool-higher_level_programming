<p align="center"><img src="https://cdn.discordapp.com/attachments/1217825406699180052/1243860284490121288/python_inherances.jpg?ex=665302a9&is=6651b129&hm=172539b08133ae51c2131295e58c1ba73b6a9de6947102dc78ab451fae21fd5d&"  alt="Python"/> </p>

<p>

**Inheritance** in object-oriented programming (OOP) is an essential concept that allows a child class to inherit methods and properties from a parent class. Here are some key points to remember about inheritance in Python:

**Definition of inheritance:**
Inheritance allows you to create a new class by extending an existing class.
The new class (subclass) inherits all methods and properties from the parent class.
This promotes code reuse and allows you to create complex relationships between objects.
**Inheritance syntax in Python:**
To create a subclass from a parent class, use the following syntax :

```
classParent:
     # Parent class methods and properties

class Child(Parent):
     # Subclass-specific methods and properties
```
La sous-classe peut ajouter ses propres méthodes et propriétés en plus de celles héritées de la classe parente.</p>

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

## ➤ EXAMPLES

**Concrete example :**
Let's imagine we have an Animal class with methods like eat() and sleep().
We can create a Dog subclass that inherits these methods and adds its own bark() method:

```
class Animal:
     def eat(self):
         print("The animal is eating.")

     def sleep(self):
         print("The animal is sleeping.")

class Dog(Animal):
     def bark(self):
         print("The dog is barking.")

my_dog = Dog()
my_dog.manger() # Calls the method inherited from the parent class
my_dog.bark() # Calls the subclass-specific method
```
In this example, Dog inherits the eat() and sleep() methods from the Animal class, while having its own bark() method

## ➤ TUTORIALS

- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Inheritance in Python](https://hub.packtpub.com/inheritance-python/)
- [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)

## ➤ LICENSE

Distributed under the MIT License. See [LICENSE](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-inheritance/LICENSE) for more information.

Copyright (c) 2024 Stephanie CARVALHO

## ➤ [AUTHORS](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/AUTHORS)

* [Stephanie Carvalho](https://github.com/Stefani-web)
