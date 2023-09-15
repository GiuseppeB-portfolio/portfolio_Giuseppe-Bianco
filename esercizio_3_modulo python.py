nome_scuola = "Epicode"
indice = 0

while indice < len(nome_scuola):
    print(nome_scuola[indice])
    indice += 1
numero = 0

while numero <= 20:
    print(numero)
    numero += 1
base = 2
esponente = 0
potenze = 0

while potenze < 10:
    risultato = base ** esponente
    print(f"2^{esponente} = {risultato}")
    esponente += 1
    potenze += 1
N = int(input("Inserisci il valore di N: "))
base = 2
esponente = 0
potenze_calcolate = 0

while potenze_calcolate < N:
    risultato = base ** esponente
    print(f"2^{esponente} = {risultato}")
    esponente += 1
    potenze_calcolate += 1
    
    studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend"]

if len(studenti) == len(corsi):
    print("Le due liste hanno la stessa lunghezza.")
else:
    print("Le due liste non hanno la stessa lunghezza.")

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]

if len(studenti) == len(corsi):
    print("Le due liste hanno la stessa lunghezza.")
else:
    print("Le due liste non hanno la stessa lunghezza.")

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"]
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]

# Aggiungi i dati mancanti ai corsi
corsi.append("Data Analyst")  # Emma segue Data Analyst
corsi.append("Backend")       # Faith segue Backend
corsi.append("Frontend")      # Grace segue Frontend
corsi.append("Cybersecurity") # Henry segue Cybersecurity

# Verifica se le due liste hanno la stessa lunghezza
if len(studenti) == len(corsi):
    print("Le due liste hanno la stessa lunghezza.")
    print("Lista corsi:", corsi)
else:
    print("Le due liste non hanno la stessa lunghezza.")

# Chiedi all'utente di inserire una stringa
input_string = input("Inserisci una stringa: ")

# Verifica la lunghezza della stringa
if len(input_string) < 6:
    # Se la stringa ha meno di 6 caratteri, visualizza un messaggio di errore
    print("La stringa deve contenere almeno 6 caratteri.")
else:
    # Estrai i primi 3 caratteri
    primi_caratteri = input_string[:3]

    # Estrai gli ultimi 3 caratteri
    ultimi_caratteri = input_string[-3:]

    # Visualizza i risultati
    risultato = primi_caratteri + "..." + ultimi_caratteri
    print("Risultato:", risultato)

# Chiedi all'utente di inserire un numero
numero = int(input("Inserisci un numero: "))

# Inizializza una lista per memorizzare i fattori
fattori = []

# Trova i fattori del numero
divisore = 2
while numero > 1:
    if numero % divisore == 0:
        fattori.append(divisore)
        numero //= divisore
    else:
        divisore += 1

# Stampa i fattori
print("Fattori del numero:", fattori)

