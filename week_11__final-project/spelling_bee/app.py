import random
import sqlite3

from flask import Flask, render_template, request, session, redirect
import requests

import config

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/', methods=['GET', 'POST'])
def index():
     # Create the wordlist database
    create_wordlist_table()

    if 'random_seven' not in session:
      generate_random_seven()
    
    random_seven = session.get('random_seven')  # Retrieve random_seven from the session


    if request.method == 'POST':
      term = request.form.get("term")
      # insert a word
      insert_word(term)
      check_user_input_in_entries(term)

      return redirect("/")
    

    elif request.method == 'GET':

      if random_seven is None:
            generate_random_seven()
            random_seven = session['random_seven']

      b1 = random_seven[0]
      b2 = random_seven[1]
      b3 = random_seven[2]
      b4 = random_seven[3]
      b5 = random_seven[4]
      b6 = random_seven[5]
      b7 = random_seven[6]

      conn = sqlite3.connect('dictionary.db')
      c = conn.cursor()
      words_results = []
      # append only the words from the database that can be constructed using no letter that is contained in random_rest:
      database_query = c.execute("SELECT word FROM entries")
      for row in database_query:
          try:
              word_letters = set(row[0])
              print(word_letters)
              if word_letters.issubset(set(random_seven)) and len(row[0]) >= 10:
                  words_results.append(row[0])
          except TypeError:
              print(f"Error processing row: {row}")

      session['words_results'] = words_results

      print(f"Possible words are {words_results}")

      wordsDay = words_results
      
      term = request.form.get("term")
      if term in words_results:
        print("yes!!!")
      else:
        print("no!!!")
      conn.close()

      # get the definition from the database:
      conn = sqlite3.connect('dictionary.db')
      c = conn.cursor()

      c.execute("SELECT definition FROM entries WHERE word=?", (term,))
      definition = c.fetchone()

      conn.close()
      
      return render_template('index.html', random_seven=random_seven, wordsDay=wordsDay, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5, b6=b6, b7=b7, definition=definition, term=term)

def create_wordlist_table():
    conn = sqlite3.connect('dictionary.db')
    c = conn.cursor()

    # Create a table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS wordlist (
            word TEXT
        )
    ''')

    conn.commit()
    conn.close()

def insert_word(term):
    conn = sqlite3.connect('dictionary.db')
    c = conn.cursor()

     # Check if the word already exists in the table
    c.execute("SELECT * FROM wordlist WHERE word=?", (term,))
    existing_row = c.fetchone()

    if existing_row:
        print(f"The word '{term}' already exists in the database.")
    else:
      # Insert a word into the table
      c.execute('INSERT INTO wordlist (word) VALUES (?)', (term,))

    conn.commit()
    conn.close()

    conn.commit()
    conn.close()


def check_user_input_in_entries(term):
    conn = sqlite3.connect('dictionary.db')
    c = conn.cursor()
    
    # check if term is in api-results database:

    c.execute("SELECT * FROM entries WHERE word=?", (term,))

    result = c.fetchone()

    if result:
      print(f"The word '{term}' exists in the table.")
    else:
      print(f"{term} is not a valid word.")

    conn.close()

def generate_random_seven():
        # Generate random_seven if it's not already in the session
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    random_seven = random.sample(alphabet, 7)
    session['random_seven'] = random_seven


@app.route('/regenerate', methods=['POST'])
def generate():
  generate_random_seven()
  return redirect("/")
