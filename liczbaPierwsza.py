
print("Sprawdzanie czy liczba jest pierwsza")
print("podaj liczbę")
liczba = int(input())

def czy_jest_pierwsza(liczba):
  """sprawdza czy liczba jest pierwsza, zwraca True jeśli tak i False jeśli nie"""
  dzielnik = 2
  while dzielnik != liczba:
    if liczba % dzielnik == 0:
      return False
    else:
      dzielnik += 1
  return True

if czy_jest_pierwsza(liczba):
  print("To jest liczba pierwsza")
else:
  print("To nie jest liczba pierwsza")