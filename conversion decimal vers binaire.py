def conversion(n):
    if n > 1:
        conversion(n // 2)
    print(n % 2, end='')
# Demande à l'utilisateur d'entrer un nombre.
nbr = int(input("Entrez un nombre decimal: "))
conversion(nbr)