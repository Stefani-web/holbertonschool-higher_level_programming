# <p align="center">Python - Data Structures: Lists, Tuples</p>

<p align="center">
<img src="https://cdn.discordapp.com/attachments/1217825406699180052/1240390914925531236/pyhton_Data_struc.jpg?ex=6646638f&is=6645120f&hm=f3e4e655af05f4e7ac6341bc5d9680f6e329093e6f9b54b9e3b22b8418a4b9c0&"  alt="Python - Lists, Tuples"/> </p>

<p>

The “Python - Data Structures: Lists, Tuples” project is a learning exercise that focuses on understanding and using **lists** and **tuples** in Python. Here is a general description of the project:

**Learning objectives:**

Understand why Python programming is popular.
Know what **lists** and **tuples** are and how to use them.
Know the differences and similarities between strings and **lists**.
Master the most common **list** methods and know how to use them.
Learn to use **lists** like stacks and queues.
Learn about **list** comprehensions and their use.
Understand when to use **tuples versus lists**.
Know what a sequence is, “**tuple** packing” and “sequence unpacking”.
Learn to use the **del** statement.

</p>

<p align="center">
<img src="https://cdn-images.threadless.com/threadless-media/artist_shops/shops/realpython/profile/logo-1613591159-afae41b42c1708f4675432b0af9e0f8e.png?v=3&d=eyJvcHMiOiBbWyJyZXNpemUiLCBbMzUwXSwge31dXSwgImZvcmNlIjogZmFsc2UsICJvbmx5X21ldGEiOiBmYWxzZX0=" alt="Logo Python"/>
</p>

<p>

The project includes several practical tasks, such as writing **functions** to print **lists of integers**, retrieving elements at a given **index**, replacing elements in a **list**, and more. These tasks help reinforce the understanding of **data structures** in **Python** and practice programming without the help of **external modules**.

For more detailed information, you can check out the official **Python** documentation on **data **structures** or educational resources like **Real Python** </p>

## ➤ INSTALLATION INSTRUCTIONS

```
Python Scripts:
- Allowed editors: vi, vim, emacs
- Python scripts must be written to run with Python 3.8.5 on Ubuntu 20.04 LTS, using python3 (version 3.8.*)
- Files must end with a new line and the first line must be exactly #!/usr/bin/python3.
- The code must follow the PEP 8 style (pycodestyle version 2.7.*).
- All files must be executable and file length will be tested with wc.
- (Prototypes for all functions must be included in a header file called lists.h, which must be protected against multiple inclusions).

```

## ➤ EXAMPLES

**1. Using Lists**

**a.** Creating and Manipulating a List
```
# Création d'une liste
my_list = [1, 2, 3, 4, 5]

# Accès aux éléments d'une liste
print(my_list[0])  # Output: 1

# Modification d'un élément dans une liste
my_list[2] = 10

# Ajout d'un élément à la fin de la liste
my_list.append(6)

# Suppression d'un élément de la liste
my_list.remove(4)

# Parcours des éléments d'une liste
for item in my_list:
    print(item)

```
**b.** List Operations
```# Concaténation de listes
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2

# Extraction d'une sous-liste (slicing)
sub_list = concatenated_list[2:5]

# Recherche d'un élément dans une liste
if 3 in concatenated_list:
    print("3 est présent dans la liste.")

# Tri d'une liste
sorted_list = sorted(concatenated_list)

# Inversion d'une liste
reversed_list = list(reversed(concatenated_list))

```
**2. Using Tuples**

**a.** Creation and Access to Elements of a Tuple
```
# Création d'un tuple
my_tuple = (1, 2, 3, 4, 5)

# Accès aux éléments d'un tuple
print(my_tuple[0])  # Output: 1

# Parcours des éléments d'un tuple
for item in my_tuple:
    print(item)

```
**b.** Operations on Tuples
```
# Concaténation de tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2

# Extraction d'une sous-tuple (slicing)
sub_tuple = concatenated_tuple[2:5]

# Recherche d'un élément dans un tuple
if 3 in concatenated_tuple:
    print("3 est présent dans le tuple.")

```
**3. Differences between Lists and Tuples**
<p> Lists and tuples are similar, but have a few important differences:

Lists are mutable, meaning they can be modified after they are created. On the other hand, tuples are immutable.
Lists are typically used for collections of items that can be changed or reordered, while tuples are often used for collections of items that do not change.
Conclusion
Lists and tuples are important data structures in Python, each with their own benefits and use cases. By understanding how to use these data structures effectively, you can write cleaner, more efficient Python code.</p>

## ➤ TUTORIALS

- [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [Data structures (until 5.3. Tuples and Sequences included)](https://docs.python.org/3/tutorial/datastructures.html)
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw&ab_channel=DerekBanas)

## ➤ LICENSE

Distributed under the MIT License. See [LICENSE](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-data_structures/LICENSE) for more information.

Copyright (c) 2024 Stephanie CARVALHO

## ➤ [AUTHORS](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-data_structures/AUTHORS)

* [Stephanie Carvalho](https://github.com/Stefani-web)
