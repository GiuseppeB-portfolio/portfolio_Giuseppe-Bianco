## 1.

nome_scuola = "Epicode"

## 2.

print("Soluzione punto 2: " + nome_scuola[0])

## 3.

print("Soluzione punto 3: " + nome_scuola[:3])

## 4.

print("Soluzione punto 4: " + nome_scuola.upper())

## 5.

print("Esecuzione metodo 1:")
x = 10
print(str(x))
x= x.__add__(2)
print(str(x))
x = x.__mul__(3)
print(str(x))
print("Esecuzione metodo 2:")
x = 10
print(str(x))
x+= 2
print(str(x))
x*=3
print(str(x))

## 6.

print("Indicare il numero di litri di benzina nel serbatorio:")
Bn_serbatorio = int(input())
print("Nel serbatoio ci sono " + str(Bn_serbatorio) +" litri di benzina.\nInserire adesso quanti kilometri vengono percorsi ogni litro:")
Efficenza = int(input())
Percorrenza = Bn_serbatorio * Efficenza
print("Con questa andatura si possono percorrere ancora " + str(Percorrenza) + " Kilometri.\nInserire adesso il costo di un litro di benzina:")
Costo = float(input())
Costo = round(Costo * 100,2)
print("Per 100 km, il costo totale della benzina è " + str(Costo) + " euro")

## 7.

print("Inserire un qualsiasi testo:")
testo=input()
print("Il risultato è:\n" + testo[:3] + "..." + testo[-3:])


## 8.

lista_stringhe = ["Epicode","Windows","Excel","Powerpoint","Word"]
for  pos in lista_stringhe:
     if len(pos) > 5 and len(pos) <8:
        print(str(pos) + " ha passato il controllo")


## 9. 

codici = ["knt-S1","cba-G9","qyr-Z8"]
cod_1 = codici[0]
print("La prima sezione è: " + str(cod_1[-3:]))
cod_2 = codici[1]
print("La seconda sezione è: " +str(cod_2[-3:]))
cod_3 = codici[2]
print("La terza sezione è: " +str(cod_3[-3:]))

## 10.

nuovi_codici = [cod_1,cod_2,cod_3]
for cod in nuovi_codici:
    print(str(cod))



## 11. 
growth = {"Tesla", "Shopify", "Block", "Etsy", "MercadoLibre","Netflix", "Amazon", "Meta Platforms", "Salesforce", "Alphabet"}
values = {"Pfizer", "Johnson & Johnson", "JPMorgan Chase & Co.","Wells Fargo & Co.", "Verizon Communications", "BP PLC","LyondellBasell Industries", "MetLife", "Interactive Brokers Group","Intel"}
tech = {"Apple", "Microsoft", "Alphabet", "Amazon", "NVIDIA", "Meta Platforms", "Tesla", "Alibaba", "Salesforce", "Advanced Micro Devices", "Intel", "PayPal", "Activision Blizzard",
         "Electronic Arts", "The Trade Desk", "Zillow Group", "Match Group", "Yelp"}
healthcare = {"UnitedHealth Group", "Johnson & Johnson", "Eli Lilly & Co.", "Novo Nordisk", "Merck & Co.", "Roche Holding", "Pfizer","Thermo Fisher Scientific", "Abbott Laboratories"}

print("Punto 1")

Punto_1 = growth.copy()
Punto_1.update(values)
if Punto_1.__len__() > 0:
    print("Le aziende Growth e Value sono :")
    for el in Punto_1:
        print(str(el))
else: print("Non esistono aziende che soddisfano la richiesta")

print("Punto 2")

Punto_2 = growth.copy()
Punto_2.intersection_update(tech)
if Punto_2.__len__() > 0:
    print("Le aziende Tecnologiche Growth sono :")
    for el in Punto_2:
        print(str(el))
else: print("Non esistono aziende che soddisfano la richiesta")

print("Punto 3")

Punto_3 = values.copy()
Punto_3.intersection_update(tech)
if Punto_3.__len__() > 0:
    print("Le aziende Tecnologiche Value sono :")
    for el in Punto_3:
        print(str(el))
else: print("Non esistono aziende che soddisfano la richiesta")

print("Punto 4")

Punto_4 = healthcare.copy()
Punto_4.difference_update(values)
if Punto_4.__len__() > 0:
    print("Le aziende Healthcare ma non Value sono :")
    for el in Punto_4:
        print(str(el))
else: print("Non esistono aziende che soddisfano la richiesta")

print("Punto 5")

Punto_5 = tech.copy()
Punto_5.intersection_update(healthcare)
if Punto_5.__len__() > 0:
    print("Le aziende sia Healthcare che Tech :")
    for el in Punto_5:
        print(str(el))
else: print("Non esistono aziende che soddisfano la richiesta")

print("Punto 6")

Punto_6_2 = tech.intersection(values)
Punto_6_1 = tech.intersection(growth)
Fine = Punto_6_1.union(Punto_6_2)
if Fine.__len__() > 0:
    print("Le aziende Tech che siano anche Growth o Values sono :")
    for el in Fine:
        print(str(el))
else: print("Non esistono aziende che soddisfano la richiesta")