def czy_jest_pierwsza(liczba):
  dzielnik = 2
  while dzielnik != liczba:
    if liczba % dzielnik == 0:
      return False
    else:
      dzielnik += 1
  return True

def main():
  print("Sprawdzanie czy liczba jest pierwsza")
  print("podaj liczbę")
  liczba = int(input())
  if czy_jest_pierwsza(liczba):
    print("To jest liczba pierwsza")
  else:
    print("To nie jest liczba pierwsza")

if __name__ == "__main__":
  main()