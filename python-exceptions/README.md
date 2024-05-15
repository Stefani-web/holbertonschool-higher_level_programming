# <p align="center">Python - Exceptions</p>

<p align="center">
<img src="https://cdn.discordapp.com/attachments/1217825406699180052/1240391008764825681/pyhton_exceptions.jpg?ex=664663a5&is=66451225&hm=9462c37ed3213ea1b76e8d49fe9a28d2929f7d42f7f082c2642e12bc5f3bccb7&"  alt="Python - Exceptions"/> </p>

<p>

The **Python Exceptions** project involves creating a program using the Python language that handles exceptions.
**Exceptions** are unanticipated events that occur during the execution of a program that can interrupt its normal flow.

In this project, you will learn how to anticipate these errors and handle them appropriately to avoid abrupt program shutdowns.

For example, you could set up try-except blocks to catch errors, finally blocks to execute code even in the event of an exception,
and even create your own custom exceptions to handle specific situations.

This project will allow you to strengthen your understanding of **exceptions** in Python and improve the robustness of your future programs.

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

1. Type Error Handling
```
try:
    x = int(input("Entrez un nombre : "))
    print("Le carré de", x, "est", x ** 2)
except ValueError:
    print("Erreur : Veuillez entrer un nombre valide.")

```
2. Handling Division by Zero Errors
```
try:
    num = int(input("Entrez un numérateur : "))
    denom = int(input("Entrez un dénominateur : "))
    result = num / denom
    print("Résultat de la division :", result)
except ZeroDivisionError:
    print("Erreur : Division par zéro non autorisée.")
except ValueError:
    print("Erreur : Veuillez entrer des nombres valides.")

```
3. Using the finally Statement
```
try:
    file = open("exemple.txt", "r")
    for line in file:
        print(line.strip())
except FileNotFoundError:
    print("Erreur : Fichier introuvable.")
finally:
    file.close()  # Fermeture du fichier même en cas d'erreur

```
4. Custom Error Handling with Custom Exceptions
```
class BalanceInsuffisanteError(Exception):
    """Exception levée lorsque le solde est insuffisant pour effectuer une opération."""

    def __init__(self, message="Solde insuffisant."):
        self.message = message
        super().__init__(self.message)

class CompteBancaire:
    """Une classe représentant un compte bancaire."""

    def __init__(self, solde=0):
        self.solde = solde

    def retirer(self, montant):
        if montant > self.solde:
            raise BalanceInsuffisanteError
        self.solde -= montant
        print("Retrait de", montant, "effectué avec succès.")

# Utilisation de l'exception personnalisée
try:
    compte = CompteBancaire(100)
    compte.retirer(150)
except BalanceInsuffisanteError as e:
    print(e)  # Affiche : Solde insuffisant.

```

## ➤ TUTORIALS

- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Learn to Program 11 Static & Exception Handling (starting at minute 7)](https://www.youtube.com/watch?v=7vbgD-3s-w4&ab_channel=DerekBanas)

## ➤ LICENSE

Distributed under the MIT License. See [LICENSE](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/LICENSE) for more information.

Copyright (c) 2024 Stephanie CARVALHO

## ➤ [AUTHORS](https://github.com/Stefani-web/holbertonschool-higher_level_programming/blob/main/python-more_data_structures/AUTHORS)

* [Stephanie Carvalho](https://github.com/Stefani-web)
