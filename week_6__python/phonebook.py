def main():

    people = {"Alice": "123-555-21", "Bob": "675-555-231", "Peter": "555-555-555", "Lucifer": "666-666-666", "Angela": "777-777-777"}

    name = input("PLease enter a name: ")

    if name in people:
        print(f"{name}'s phone number is {people[name]}") # Why does that give back the value 'number' and not the key 'name'? 
    else:
        print(f"{name} not found!")

main()