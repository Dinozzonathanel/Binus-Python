
#Data Science Exercise

import pandas as pd

cdata = {
    "Country" : ["Indonesia", "United States", "Japan", "China", "France", "Russia", "England", "Sweden", "Germany", "India"],
    "Capital city" : ["Jakarta", "Washington, D.C", "Tokyo", "Beijing", "Paris", "Moscow", "London", "Stockholm", "Germany", "New Delhi"],
    "Continent" : ["Asia", "America", "Asia", "Asia", "Europe", "Europe", "Europe", "Europe", "Europe", "Asia"],
    "Population (mil)" : [283, 340, 124, 1406, 70, 143, 67, 10, 83, 1451],
    "Area" : [1905, 9867, 337, 9597, 551, 17001, 130, 450, 357, 3287]

}

df = pd.DataFrame(cdata)
mean = df.Area.mean()
std = df["Population (mil)"].std()

print(df)
print(mean)
print(std)

df.to_csv('file1.csv')

#Data handling exercise 1

def save(Self):
  file = open("data.txt", "w")
  file.write(str(userdata))
  file.close()

userdata = None

n = True
while n:
    menuchoosen = input("""
Hello and welcome to the idk program! Pick a menu:
  a. Input new data
  b. Read data
  c. Edit data
  d. Delete data
  e. End program
>> """)

    if (menuchoosen == "a"):
      Name = input("Name :")
      Age = input("Age :")
      Adress = input("Adress :")
      Email = input("Email :")
      userdata = [Name, Age, Adress, Email]
      save(userdata)
    elif (menuchoosen == "b"):
      if (userdata == None):
        print("There is no data")
      else:
        file = open("data.txt", "r")
        text = file.read()
        print(text)
        file.close()
    elif (menuchoosen == "c"):
      Name = input("New Name :")
      Age = input("New Age :")
      Adress = input("New Adress :")
      Email = input("New Email :")
      userdata = [Name, Age, Adress, Email]
      save(userdata)
    elif (menuchoosen == "d"):
        userdata = None
        open("data.txt", "w").close()  # clear file
        print("Data deleted.")
    elif (menuchoosen == "e"):
      print("Thank you for using this program!")
      n = False
