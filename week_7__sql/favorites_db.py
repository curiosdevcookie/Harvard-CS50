from cs50 import SQL

db = SQL("sqlite:///favorites.db")

favorite = input("Favorite: ").lower()

rows = db.execute("SELECT * FROM favorites WHERE problem = 'filter';")
for i in range(0, len(rows)):
  print(rows[i]["language"])

rows = db.execute("SELECT COUNT(*) AS n FROM favorites WHERE problem = ?;", favorite) # always returns list of dictionaries with select. 
row = rows[0] # Returns the first and only row because COUNT(*) returns a single row with a single column
print(f"How many favored your choice: {row['n']}.")

# ACID
# Atomicity: All or nothing
# Consistency: Database is always in a valid state
# Isolation: Transactions can't interfere with each other
# Durability: Once a transaction is committed, it's permanent
