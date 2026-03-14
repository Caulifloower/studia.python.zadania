print("Ciąg fibonnaciego do ntego wyrazu")
print("Podaj wartość n")
n = int(input())
wynik = [1,1]
if n == 1:
  wynik.remove[1]
else:
  i = 2
  while i < n:
    x = wynik[i - 1]
    y = wynik[i - 2]
    wynik.append(x + y)
    i += 1

print(wynik)