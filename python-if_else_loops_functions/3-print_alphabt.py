#!/usr/bin/python3
# Boucle sur les valeurs ASCII des caractères de 'a' à 'z'
for i in range(ord('a'), ord('z')+1):
    # Vérifie si le caractère correspondant n'est pas 'q' ou 'e'
    if chr(i) not in 'qe':
        # Imprime le caractère sans saut de ligne
        print(chr(i), end='')
