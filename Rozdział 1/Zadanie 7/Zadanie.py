from random import randint

def main():
  print("Oto 5 wylosowanych liczb całkowitych z przedziału od 1 do 100:\n")
  for i in range(5):
    print(randint(1, 100))
    
main()