

"""
Usando i set devo provare a capire chi ha passato entrambi gli esami. 
Gli studenti che hanno passato almeno un esame
Gli studenti che hanno passato l'esame 1 ma non il due.
"""

esame1 = ["Irene", "Paolo", "Luca", "Irene", "Marco"]
esame2 = ["Paolo", "Luca", "Giulia", "Marco", "Giulia"]

set_esame1 = set(esame1)
set_esame2 = set(esame2)

print(f"ESAME 1: {esame1}")
print(f"ESAME 2: {esame2}")

lista = []
for i in set_esame2:
    if i not in set_esame1:
        lista.append(i)
for i in set_esame1:
    if i not in set_esame2:
        lista.append(i)
set_3 = set(lista)
entrambi = set_esame1 - set_3
print(f"ENTRAMBI: {entrambi}")
#tutto questo lo riassumo con set_esame1 & set_esame2 che è l'intersezione

nome_studente = str(input("Inserire nome studente ricercato: "))
if nome_studente in esame1 or nome_studente in esame2:
    print(f" {nome_studente} ha passato almeno un esame")

else:
    print(f" {nome_studente} non ha passato alcun esame")
#questo me lo evitavo con set_esame1 | set_esame2 che è l'unione

print(f"{set_esame1 - set_esame2} ha passato l'esame 1, ma non il 2")

