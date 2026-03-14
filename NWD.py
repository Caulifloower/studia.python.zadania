print("NWD")
print("Podaj liczbę 1:")
liczba1 = int(input())
print("Podaj liczbę 2:")
liczba2 = int(input())

def dzielniki(liczba):
  """wypisuje rozkład na dzielniki podanej liczby"""
  dzielniki = []
  dzielnik = 2
  while liczba > 1:
    if liczba % dzielnik == 0:
      liczba /= dzielnik
      dzielniki.append(dzielnik)
    else:
      dzielnik += 1
  return dzielniki

dzielniki_liczby1 = dzielniki(liczba1)
dzielniki_liczby2 = dzielniki(liczba2)

def czy_sa_wspolne_dzielniki(zbior1, zbior2):
  """Sprwadza czy 2 zbiory posiadają chociaż jedny wspólny dzielnik, zwraca True jeśli tak i False jeśli nie"""
  for element1 in zbior1:
    if element1 in zbior2:
      return True
  return False

dzielnik = 1
wspolne_dzielniki = []
print("są wspólne dzielniki")
while czy_sa_wspolne_dzielniki(dzielniki_liczby1, dzielniki_liczby2):
  if dzielnik in dzielniki_liczby1 and dzielnik in dzielniki_liczby2:
    dzielniki_liczby1.remove(dzielnik)
    dzielniki_liczby2.remove(dzielnik)
    wspolne_dzielniki.append(dzielnik)
  else:
    dzielnik += 1
nwd = 1
for wspolny_dzielnik in wspolne_dzielniki:
  nwd *= wspolny_dzielnik

print(nwd)