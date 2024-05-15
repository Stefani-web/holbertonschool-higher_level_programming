# <p align="center">Python - Classes and Objects</p>

<p align="center">
<img src="https://cdn.discordapp.com/attachments/1217825406699180052/1240391076007641159/python_classes.jpg?ex=664663b5&is=66451235&hm=5d226da3f45aca2e3fa20abe3ef7fa18e1d680cbc87c77c3f1c4e2bfae42e8c7&"  alt="Python - Classes and Objects"/> </p>

<p>

The **"Python - Classes and Objects"** project involves exploring and putting into practice the fundamental concepts of
 object-oriented programming (OOP) using the Python programming language. In this project, you will learn how to define classes and create objects,
 which are **instances of these classes**.

 You'll learn how to define attributes and methods in a class, and how to access these attributes and methods from the objects you create.
 Using real-world examples, you will also learn the principles of encapsulation, inheritance, and polymorphism.
 Encapsulation consists of grouping data (attributes) and the operations (methods) that manipulate them into a single entity, the class, to make them more modular and easy to manage.

 Inheritance allows you to create new classes based on existing classes, reusing and extending their functionality. Polymorphism allows you to use the same interface for objects of different **classes**, providing increased flexibility and extensibility in your code. This project will give you a solid understanding of basic OOP concepts in Python, which will allow you to create programs that are more modular, more flexible, and easier to maintain.

</p>

<p align="center">
<img src="https://cdn-images.threadless.com/threadless-media/artist_shops/shops/realpython/profile/logo-1613591159-afae41b42c1708f4675432b0af9e0f8e.png?v=3&d=eyJvcHMiOiBbWyJyZXNpemUiLCBbMzUwXSwge31dXSwgImZvcmNlIjogZmFsc2UsICJvbmx5X21ldGEiOiBmYWxzZX0=" alt="Logo Python"/>
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
Create an instance of Square :
```
# Création d'une instance de Square avec la taille par défaut
square_default = Square()

# Création d'une instance de Square avec une taille spécifiée
square_custom = Square(5)

```
Using size properties:
```
# Récupérer la taille du carré
print(square_custom.size)  # Output: 5

# Définir une nouvelle taille pour le carré
square_custom.size = 7
print(square_custom.size)  # Output: 7

# Essayer de définir une taille non valide
try:
    square_custom.size = -3
except ValueError as e:
    print(e)  # Output: size must be >= 0

try:
    square_custom.size = "ten"
except TypeError as e:
    print(e)  # Output: size must be a number
```
Calculate the area of the square:
```
# Calculer l'aire d'un carré
print(square_custom.area())  # Output: 49

```
Classe Square:
```
class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with a given size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Compare equality based on area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Compare inequality based on area."""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Compare greater than based on area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Compare greater than or equal based on area."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """Compare less than based on area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Compare less than or equal based on area."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

```

## ➤ TUTORIALS

- [Object Oriented Programming](https://python.swaroopch.com/oop.html)
- [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE&ab_channel=DerekBanas)
- [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s&ab_channel=Socratica)
- [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk&ab_channel=MITOpenCourseWare)
- [Classes and Attributes (French)](https://www.youtube.com/watch?v=91dPooHyNIo&ab_channel=FormationVid%C3%A9o)
- [Classes (French)](https://www.youtube.com/watch?v=KwglfT76iv8&ab_channel=SimpleTech)

## ➤ LICENSE

Distributed under the MIT License. See [LICENSE](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-classes/LICENSE) for more information.

Copyright (c) 2024 Stephanie CARVALHO

## ➤ [AUTHORS](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-classes/AUTHORS)

* [Stephanie Carvalho](https://github.com/Stefani-web)
