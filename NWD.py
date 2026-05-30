def dzielniki(liczba):
  dzielniki = []
  dzielnik = 2
  while liczba > 1:
    if liczba % dzielnik == 0:
      liczba /= dzielnik
      dzielniki.append(dzielnik)
    else:
      dzielnik += 1
  return dzielniki

def czy_sa_wspolne_dzielniki(zbior1, zbior2):
  for element1 in zbior1:
    if element1 in zbior2:
      return True
  return False

def main():
  print("NWD")
  print("Podaj liczbę 1:")
  liczba1 = int(input())
  print("Podaj liczbę 2:")
  liczba2 = int(input())
  dzielniki_liczby1 = dzielniki(liczba1)
  dzielniki_liczby2 = dzielniki(liczba2)
  dzielnik = 1
  wspolne_dzielniki = []
  print("NWD:")
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

if __name__ == "__main__":
  main()