def rekurencja(liczba):
  if liczba > 1:
    return liczba * rekurencja(liczba - 1)
  else:
    return liczba

def main():
  print("SILNIA:")
  print("Podaj liczbę")
  liczba = int(input())
  licznik = liczba
  wynik = 1

  print("wynik:")
  print("iteracja")
  while licznik > 1:
    wynik *= licznik
    licznik -= 1
  print(wynik)

  print("rekurencja")
  wynik = rekurencja(liczba)
  print(wynik)

if __name__ == "__main__":
  main()