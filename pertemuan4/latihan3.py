continuem = "y"

while(True):
    if (continuem == "y"):
       number = int(input("number:"))

       number / 2

       if (number % 2 == 0):
            print("genap")
            continuem = input("would you like me to repeat? (y/n)")
       else:
            print("ganjil")
            continuem = input("would you like me to repeat? (y/n)")
    else:
        print("Program was End")
        break
