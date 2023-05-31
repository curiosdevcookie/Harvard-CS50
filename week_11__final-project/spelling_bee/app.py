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
    create_wordlist_database()
    create_api_results_database()

    if 'random_seven' not in session:
      generate_random_seven()
    else:
      random_seven = session['random_seven']  # Retrieve random_seven from the session


    if request.method == 'POST':
      term = request.form.get("term")
      # insert a word
      insert_word(term)
      check_user_input_in_api_results(term)

      return redirect("/")
    

    elif request.method == 'GET':

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
          word_letters = set(row[0])
          if word_letters.issubset(set(random_seven)):
              words_results.append(row[0])

      session['words_results'] = words_results

      print(f"Possible words are {words_results}")

      wordsDay = words_results
      
      term = request.form.get("term")
      if term in words_results:
        print("yes!!!")
      else:
        print("no!!!")
      conn.close()

      # get the definition, example, permalink from the database:
      conn = sqlite3.connect('dictionary.db')
      c = conn.cursor()

      c.execute("SELECT definition FROM api_results WHERE word=?", (term,))
      definition = c.fetchone()

      c.execute("SELECT example FROM api_results WHERE word=?", (term,))
      example = c.fetchone()

      c.execute("SELECT permalink FROM api_results WHERE word=?", (term,))
      permalink = c.fetchone()

      conn.close()
      
      return render_template('index.html', random_seven=random_seven, wordsDay=wordsDay, b1=b1, b2=b2, b3=b3, b4=b4, b5=b5, b6=b6, b7=b7, definition=definition, example=example, permalink=permalink, term=term)


@app.route('/api_call')
def api_call():
    try:
          all_words = []
          number_of_words = 300

          # Get number_of_words = x  from the database:
          while len(all_words) < number_of_words:

            # API call code
            url = 'https://urban-dictionary7.p.rapidapi.com/v0/random'
            headers = {
              "X-RapidAPI-Key":  config.api_key,
              "X-RapidAPI-Host": config.host
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Check for any HTTP errors

            api_result = response.json()

            # Check if the word contains whitespace,or other non letters
            word = api_result['list'][0]['word'].upper()

            if not any([char in word for char in [' ', '/', '-', '—', '+', '#', '=', '&', '@', '$', '\'', ';']]) and len(word)>3:
                all_words.append(word)

                # Insert the API result into the database
                insert_api_result(api_result)

          print(all_words)
          return 'API call executed successfully'
    
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API call: {str(e)}")
        return 'API call failed'
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 'API call failed'

def create_wordlist_database():
    conn = sqlite3.connect('wordlist.db')
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
    conn = sqlite3.connect('wordlist.db')
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


def create_api_results_database():
    conn = sqlite3.connect('dictionary.db')
    c = conn.cursor()

    # Create a table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS api_results (
            word TEXT,
            definition TEXT,
            example TEXT,
            permalink TEXT,
            UNIQUE(word)
        )
    ''')

    conn.commit()
    conn.close()


def insert_api_result(api_result):
    conn = sqlite3.connect('dictionary.db')
    c = conn.cursor()

    # Extract the relevant data from the API result
    word = api_result['list'][0]['word'].upper()
    definition = api_result['list'][0]['definition']
    example = api_result['list'][0]['example']
    permalink = api_result['list'][0]['permalink']

    # Check if the word already exists in the table
    c.execute("SELECT * FROM api_results WHERE word=?", (word,))
    existing_row = c.fetchone()

    if existing_row:
        print(f"The word '{word}' already exists in the database.")
    else:
        # Insert the API result into the table
        c.execute('INSERT INTO api_results (word, definition, example, permalink) VALUES (?, ?, ?, ?)',
                  (word, definition, example, permalink))
        print(f"The word '{word}' was inserted into the database.")

    conn.commit()
    conn.close()

def check_user_input_in_api_results(term):
    conn = sqlite3.connect('dictionary.db')
    c = conn.cursor()
    
    # check if term is in api-results database:

    c.execute("SELECT * FROM api_results WHERE word=?", (term,))

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
