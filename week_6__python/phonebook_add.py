import csv

file = open("phonebook.csv", "a")

name = input("Please provide a name: ")
number = input("Please provide a number: ")

adder = csv.writer(file)

adder.writerow([name, number])

file.close()


#alternatively, for automatically closing the file after writing:

with open("phonebook.csv", "a") as file:
    name = input("Please provide a name: ")
    number = input("Please provide a number: ")
    adder = csv.writer(file)
    adder.writerow([name, number])

#alternatively, for writing differently to the file:

with open("phonebook.csv", "a") as file:
    name = input("Please provide a name: ")
    number = input("Please provide a number: ")
    adder = csv.DictWriter(file, fieldnames=["name", "number"])
    adder.writerow({"name": name, "number": number})