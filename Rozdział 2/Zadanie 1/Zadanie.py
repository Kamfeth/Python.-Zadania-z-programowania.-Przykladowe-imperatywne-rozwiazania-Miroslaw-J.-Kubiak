def main():
  a = int(input("Wprowadź wartość pierwszego boku trójkąta: "))
  b = int(input("Wprowadź wartość drugiego boku trójkąta: "))
  c = int(input("Wprowadź wartość trzeciego boku trójkąta: "))
  print("Wprowadzone wartości boków ", end = "")
  print("spełniają równanie Pitagorasa") if a ** 2 + b ** 2 == c ** 2 else print("nie spełniają równania Pitagorasa")

main()