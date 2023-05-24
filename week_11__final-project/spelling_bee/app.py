import sqlite3
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
     # Create the wordlist database
    create_wordlist_database()
    if request.method == 'POST':
      term = request.form.get("term")
      # insert a word
      insert_word(term)
      print(f"{term} was inserted into wordlist.")
      return render_template('index.html', term=term)
    elif request.method == 'GET':
      return render_template('index.html')

@app.route('/api_call')
def api_call():
    try:
        # API call code
        url = 'https://urban-dictionary7.p.rapidapi.com/v0/random'
        headers = {
          "X-RapidAPI-Key": "95d2126b2emsha1b4c9955aaf227p13b388jsnbdc54fbaecce",
          "X-RapidAPI-Host": "urban-dictionary7.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for any HTTP errors

        api_result = response.json()
        print(response.json())

        # Insert the API result into the database
        insert_api_result(api_result)

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
    conn = sqlite3.connect('api_results.db')
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
    conn = sqlite3.connect('api_results.db')
    c = conn.cursor()

    # Extract the relevant data from the API result
    word = api_result['list'][0]['word']
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


if __name__ == '__main__':



    # Create the API results database
    create_api_results_database()

