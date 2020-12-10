import sys
import random
import time

class GuessingGame:
    def guessinggame1(self):

        randomnum = random.randint(1, 5)

        print("\n")
        print("*"*100,"\n")
        print(f"A brincadeira é você adivinhar um número entre 1 e 5. Vamos tentar?\n")
        print("*"*100,"\n")
        print("Carregando...\n")
        time.sleep(6)
        
        while True:
            try:
                guessnum = int(input(f"Digite um número entre 1 and 5: "))
                if 0 < guessnum < 6:
                    if guessnum == randomnum:
                        print("\nVocê é um gênio.\n")
                        break
                else:
                    print("\nHeyyy. Somente números entre 1 e 5!!\n")
                    continue
            except (TypeError, ValueError):
                print("\nXX Por favor, entre somente com números. XX\n")
            else:
                print("\nNão foi dessa vez. Tente novamente!!!\n")


    def guessinggame2(self):
        
        try:
            startnum = int(sys.argv[1])
            endnum = int(sys.argv[2])

            randomnum = random.randint(startnum, endnum)

            print("\n")
            print("*"*100,"\n")
            print(f"A brincadeira é você adivinhar um número entre {startnum} e {endnum}. Vamos tentar?\n")
            print("*"*100,"\n")
            print("Carregando...")
            time.sleep(3)
        except (IndexError, UnboundLocalError):
            print("\nPlease include the numbers before run the program")


        while True:
            try:
                guessnum = int(input(f"Digite um número entre {startnum} e {endnum}: "))
                if guessnum == 0 or guessnum > endnum:
                    print(f"Heyyyyy!! Por favor entre com um número entre {startnum} e {endnum}.")
                    continue
                print("Checando o número....\n")
                time.sleep(1)
                if guessnum == randomnum:
                    print("="*100)
                    print(f"\nUAUUUU. Você adivinhou. Parabénsssss!!! O número gerado foi {randomnum} e o seu foi {guessnum}.\n")
                    print("="*100)
                    break
            except (ValueError, ZeroDivisionError):
                print("Ooooops. Error. Please type a number and not 0.")
            else:
                print(f"Tente novamente!!! Número {guessnum} não é correto.\n")


guessinggame = GuessingGame()
guessinggame.guessinggame1()
