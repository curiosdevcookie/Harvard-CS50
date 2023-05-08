import csv

# with open("favorites.csv", "r") as favorites_file:
#     reader = csv.reader(favorites_file)
#     next(reader)
#     for row in reader:
#         favorite = row[1]
#         print(favorite)

# with open("favorites.csv", "r") as favorites_file:
#     reader = csv.DictReader(favorites_file)
#     for row in reader:
#         favorite = row["language"]
#         print(favorite)
        
with open("favorites.csv", "r") as favorites_file:
    reader = csv.DictReader(favorites_file)
    counts = {}


    # for row in reader:
    #     favorite = row["language"]
    #     print(favorite)
    #     if favorite == "scratch":
    #         scratch += 1
    #     elif favorite == "python":
    #         python += 1
    #     elif favorite == "c":
    #         c += 1
    #     else:
    #         print("unknown language")
    # print(scratch, python, c)

    for row in reader:
        favorite = row["language"]
        # print(favorite)
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1
    # print(counts)

    # def get_value(favorite):
    #     return counts[favorite]
    # for favorite in sorted(counts, key=get_value, reverse=True): # for…in is the pythonic way to iterate over the keys
    #     print(f"{favorite}: {counts[favorite]}")
    

    for favorite in sorted(counts, key=lambda language: counts[language], reverse=True): # for…in is the pythonic way to iterate over the keys
        print(f"{favorite}: {counts[favorite]}")

    # user input:

    favorite = input("Your Favorite: ")

    if favorite in counts:
        print(f"Your favorite: {favorite} | others liked it: {counts[favorite]}")
    