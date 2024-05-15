
# <p align="center">Python - More Data Structures: Set, Dictionary</p>

<p align="center">
<img src="https://cdn.discordapp.com/attachments/1217825406699180052/1240391008500449422/pyhton_more_data_struct.jpg?ex=664663a5&is=66451225&hm=913190e25160948aff928dcb712f1dbad5548963765ab7686ba5b245f99758d0&"  alt="Python - Set, Dictionary"/> </p>

<p>

**The "Python - More Data Structures:** **Set, Dictionary"** project aims to deepen the understanding of advanced **data structures** in Python, including sets and **dictionaries**.

These data structures are crucial for the efficient manipulation and storage of data in many programming problems.

The project includes several exercises that explore different features and operations available with **sets and dictionaries**.

This includes operations such as adding, removing, and finding elements, as well as set operations such as union, intersection, and difference. Additionally, it covers advanced concepts such as manipulating nested **dictionaries** and sorting items alphabetically or **numerically**.

Through this project, developers will improve their understanding of **sets and dictionaries** in **Python**, allowing them to solve problems efficiently and elegantly, using the right data structures for each situation.

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

**1. Using Sets**

**a.** Creation and Manipulation of a Set
```
# Création d'un ensemble
my_set = {1, 2, 3, 4, 5}

# Ajout d'éléments à un ensemble
my_set.add(6)

# Suppression d'un élément d'un ensemble
my_set.remove(3)

# Parcours des éléments d'un ensemble
for item in my_set:
    print(item)

# Vérification d'appartenance d'un élément à un ensemble
if 4 in my_set:
    print("4 appartient à l'ensemble.")

```
**b.** Operations on Sets
```
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union
union_set = set1.union(set2)

# Intersection
intersection_set = set1.intersection(set2)

# Différence
difference_set = set1.difference(set2)

# Vérifier si un ensemble est un sous-ensemble d'un autre
is_subset = set1.issubset(set2)

```
**2. Use of dictionaries**

**a.** Creating and Manipulating a Dictionary
```
# Création d'un dictionnaire
my_dict = {"nom": "Alice", "âge": 30, "ville": "Paris"}

# Accéder aux valeurs d'un dictionnaire
print(my_dict["nom"])  # Output: Alice

# Modifier une valeur dans un dictionnaire
my_dict["âge"] = 25

# Ajouter un nouvel élément au dictionnaire
my_dict["email"] = "alice@example.com"

# Supprimer un élément du dictionnaire
del my_dict["ville"]

```
**b.** Navigating the Keys and Values of a Dictionary
```
# Parcourir les clés d'un dictionnaire
for key in my_dict:
    print(key)

# Parcourir les valeurs d'un dictionnaire
for value in my_dict.values():
    print(value)

# Parcourir à la fois les clés et les valeurs
for key, value in my_dict.items():
    print(key, ":", value)

```
**c.** Useful Dictionary Methods
```
# Vérifier si une clé existe dans un dictionnaire
if "nom" in my_dict:
    print("La clé 'nom' existe dans le dictionnaire.")

# Obtenir la longueur d'un dictionnaire (nombre de paires clé-valeur)
dict_length = len(my_dict)

# Copier un dictionnaire
copy_dict = my_dict.copy()

```

## ➤ TUTORIALS

- [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Lambda, filter, reduce and map](https://python-course.eu/advanced-python/lambda-filter-reduce-map.php)
- [Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=1GAC6KQUPeg)

## ➤ LICENSE

Distributed under the MIT License. See [LICENSE](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/LICENSE) for more information.

Copyright (c) 2024 Stephanie CARVALHO

## ➤ [AUTHORS](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/AUTHORS)

* [Stephanie Carvalho](https://github.com/Stefani-web)
