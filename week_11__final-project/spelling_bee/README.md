# Urban SpellingBee adaptation

This is a version of the game Spelling Bee with the Urban Dictionary as its lexicon.

## Installation

To install the game, you need to install the required packages via your terminal. You can do this by running

```bash
pip install -r requirements.txt
```

## Set up the database

To install the database, you need to run the following commands in your terminal:

```bash
wget "https://www.dropbox.com/s/tiqdlgzbo40ak8g/dictionary.db" -O dictionary.db
```

In `app.py`, set the variable `PATH_TO_DATABASE` to the path to the database.

## Run the app

To run the app, you need to run the following command in your terminal:

```bash
flask run
```

## Final remarks

This is a work in progress. The game is playable, but there are still some bugs to fix and features to add.
