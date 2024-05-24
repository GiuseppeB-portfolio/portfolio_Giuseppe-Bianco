from math import sqrt

hello_message = """
Questa è la mia calcolatrice!

Ecco cosa puoi fare:

- Addizione, seleziona 1;
- Sottrazione, seleziona 2;
- Moltiplicazione, seleziona 3;
- Divisione, seleziona 4;
- Calcolo Esponenziale, seleziona 5;
- Radice Quadrata, seleziona 6;
- Radice Cubica, selezione 7;
- Termina calcolo digitare ESC;
"""


while True:
    print(hello_message)

    action = input("Operazione da effettuare: ")

    if action == "1":
        print("\nHai scelto: Addizione\n")
        a = float(input("Inserisci il Primo Numero -> "))
        b = float(input("Inserisci il Secondo Numero -> "))
        print("Il risultato dell'Addizione è: ", str(a + b))
    elif action == "2":
        print("\nHai scelto: Sottrazione\n")
        a = float(input("Inserisci il Primo Numero -> "))
        b = float(input("Inserisci il Secondo Numero -> "))
        print("Il risultato dell'Sottrazione è: ", str(a - b))
    elif action == "3":
        print("\nHai scelto: Moltiplicazione\n")
        a = float(input("Inserisci il Primo Numero -> "))
        b = float(input("Inserisci il Secondo Numero -> "))
        print("Il risultato dell'Moltiplicazione è: ", str(a * b))
    elif action == "4":
        print("\nHai scelto: Divisione\n")
        a = float(input("Inserisci il Primo Numero -> "))
        b = float(input("Inserisci il Secondo Numero -> "))
        print("Il risultato dell'Divisione è: ", str(a / b))
    elif action == "5":
        print("\nHai scelto: Calcolo Esponenziale\n")
        a = float(input("Inserisci la Base -> "))
        b = float(input("Inserisci l'Esponente -> "))
        print("Il risultato del Calcolo Esponenziale è: ", str(a ** b))
    elif action == "6":
        print("\nHai scelto: Radice Quadrata\n")
        a = float(input("Inserisci il Numero -> "))
        print("Il risultato dell'operazione è: ", str(sqrt(a)))
    elif action == "7":
        print("\nHai scelto: Radice Cubica\n")
        a = float(input("Inserisci il numero -> "))
        print("Il risultato dell'operazione è: ", str(sqrt(a)))
    elif action == "ESC":
        print("\nL'Applicazione verrà chiusa!\n")
        break

    new_action = input("\nVuoi continuare ad utilizzare la calcolatrice? S/N ")
    if new_action == "S" or new_action == "s":
        print("Sto tornando al menù principale!\n")
        continue
    else:
        print("A presto!\n")
        break