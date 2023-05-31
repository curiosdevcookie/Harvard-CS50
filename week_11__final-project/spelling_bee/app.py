import random
import sqlite3

from flask import Flask, render_template, request, session, redirect
import string



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
      session['term'] = term
      print(f"term is {term}")

      words_results = session.get('words_results')
      if term not in words_results:
        print(f"\n word {term} is not found!\n")
        return redirect("/")
      else:
        print(f"\n word {term} was found!\n")
        insert_word(term)
        get_definition(term)
        get_word_from_wordlist(term)

      session['definition'] = get_definition(term)
      session['word'] = get_word_from_wordlist(term)
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

      words_results = []

      conn = sqlite3.connect('dictionary.db')
      c = conn.cursor()

      # append only the words from the database that can be constructed using no letter that is contained in random_rest:
      database_query = c.execute("SELECT word FROM entries")
      for row in database_query:
          try:
              word_letters = set(row[0])
              if word_letters.issubset(set(random_seven)):
                words_results.append(row[0])
          except TypeError:
            print(f"Error processing row: {row}")
      session['words_results'] = words_results
      conn.close()

      words = []
      conn = sqlite3.connect('dictionary.db')
      c = conn.cursor()

      c.execute("SELECT word FROM wordlist")
      word_rows = c.fetchall()

      for row in word_rows:
          word = get_word_from_wordlist(row[0])
          if word:
              words.append(word)

      conn.close()

      return render_template('index.html', random_seven=random_seven, words_results=words_results, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5, b6=b6, b7=b7, definition=session.get('definition'), word=session.get('word'), words=words)

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

def generate_random_seven():
    vowels = ['A', 'E', 'I', 'O', 'U']
        # Generate random_seven if it's not already in the session
    alphabet = string.ascii_uppercase

    random_seven = random.sample(alphabet, 7)
    # check if there is at least two vowels in the random_seven:
    if len(set(random_seven).intersection(vowels)) < 2:
        return generate_random_seven()
    print(f"random_seven is {random_seven}")

    # random_rest = list(set(alphabet) - set(random_seven))
    # print(f"random_rest is {random_rest}")
    
    session['random_seven'] = random_seven
    # session['random_rest'] = random_rest


@app.route('/regenerate', methods=['POST'])
def generate():
  generate_random_seven()
  delete_all_words()
  return redirect("/")


 # get the definition of term from the table entries if term is in words_results:
def get_definition(term):
  print(f"term is {term}")
    # get the definition from the database:
  conn = sqlite3.connect('dictionary.db')
  c = conn.cursor()

  c.execute("SELECT definition FROM entries WHERE word=?", (term,))
  definition = c.fetchone()
  print(f"definition is {definition}")


  conn.close()
  return definition

def get_word_from_wordlist(term):

  print(f"term is {term}")
  conn = sqlite3.connect('dictionary.db')
  c = conn.cursor()

  c.execute("SELECT word FROM wordlist WHERE word=?", (term,))
  word = c.fetchone()
  if word:
    # slice the word from the tuple:
    word = word[0]
  else:
     word = None

  conn.close()

  return word

def delete_all_words():
    conn = sqlite3.connect('dictionary.db')
    c = conn.cursor()

    c.execute("DELETE FROM wordlist")

    conn.commit()
    conn.close()