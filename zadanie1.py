import statistics

print("podaj listę ocen oddzielonych przecinkiem")
lista_ocen_string=input()
lista_ocen = lista_ocen_string.split(',')
lista_ocen_int = []
for ocena in lista_ocen:
  lista_ocen_int.append(int(ocena))
print(lista_ocen_int)

print("Średnia: ")
print(sum(lista_ocen_int)/len(lista_ocen_int))
suma_ocen = 0
liczba_ocen = 0
for ocena in lista_ocen_int:
  suma_ocen += ocena
  liczba_ocen += 1
srednia = suma_ocen/liczba_ocen
print(srednia)

print("MAX: ")
max = sorted(lista_ocen_int)[len(lista_ocen_int)-1]
print(max)

print("MIN: ")
min = sorted(lista_ocen_int, reverse=True)[len(lista_ocen_int)-1]
print(min)

print("Mediana: ")
print(statistics.median(lista_ocen_int))

wartosci_mediany = []
if len(lista_ocen_int) % 2 == 0:
  wartosci_mediany.append(sorted(lista_ocen_int)[int(len(lista_ocen_int)/2)])
  wartosci_mediany.append(sorted(lista_ocen_int)[int(len(lista_ocen_int)/2 - 1)])
else:
  wartosci_mediany.append(sorted(lista_ocen_int)[int((len(lista_ocen_int) - 1)/2)])
mediana = sum(wartosci_mediany)/len(wartosci_mediany)
print(mediana)

print("Liczba ocen powyżej średniej: ")
liczba_ocen_powyzej_sredniej = 0
for ocena in lista_ocen_int:
  if ocena > srednia:
    liczba_ocen_powyzej_sredniej += 1
print(liczba_ocen_powyzej_sredniej)

slownik = {}
slownik["średnia"] = srednia
slownik["max"] = max
slownik["min"] = min
slownik["mediana"] = mediana
slownik["liczba ocen powyżej średniej"] = liczba_ocen_powyzej_sredniej

print(slownik)