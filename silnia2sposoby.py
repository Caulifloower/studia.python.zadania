print("SILNIA:")
print("Podaj liczbę")
liczba = int(input())
licznik = liczba
wynik = 1

print("iteracja")
while licznik > 1:
  wynik *= licznik
  licznik -= 1
print("wynik:")
print(wynik)

print("rekurencja")
def rekurencja(liczba):
  """rekurencyjnie wylicza silnię"""
  if liczba > 1:
    return liczba * rekurencja(liczba - 1)
  else:
    return liczba

wynik = rekurencja(liczba)
print(wynik)