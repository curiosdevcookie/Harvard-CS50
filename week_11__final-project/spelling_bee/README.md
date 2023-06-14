# Urban Spelling Bee

We love playing the [Spelling Bee of the NY Times](https://www.nytimes.com/puzzles/spelling-bee).

This is a version of Spelling Bee with the Urban Dictionary as its lexicon.

As we aren't English native speakers and we like to learn new words, the player is provided with a word's definition if the word is found in the dictionary.

Protip: Click on the bee to get a new set of letters.

## Run the app locally

### Installation

To install the game, you need to install the required packages via your terminal. You can do this by running

```bash
pip install -r requirements.txt
```

### Set up the database

To install the database, you need to run the following commands in your terminal:

```bash
wget "https://www.dropbox.com/s/tiqdlgzbo40ak8g/dictionary.db" -O dictionary.db
```

### Configuration

Set the variable `is_local` to `True`.

```python
is_local = True
```

This is important for app to choose the correct path to the database.

### Run the app

To run the app, you need to run the following command in your terminal:

```bash
flask run -p 8000
```

You can now access the app on `http://127.0.0.1:8000/`.

## Run the app via docker

### Installation

Run the following command in your terminal to build the container:

```bash
docker build -t spelling-bee .
```

### Configuration

In `app.py`, set the variable `is_local` to `False`.

```python
is_local = False
```

### Run the app

Run the following command in your terminal to run the container:

```bash
docker run -p 8000:8000 -v "$(pwd)/data:/data" spelling-bee
```

The `$(pwd)/data:/data` part in the docker run command is used to mount the  data directory to the /data directory inside the Docker container. This allows the container to access the dictionary.db.

You can now access the app on `http://127.0.0.1:8000/`.

## How to play

The game is played as follows:

1. Create as many words as you can by clicking on the given letters.
2. The word must be at least 4 letters long.
3. The word must contain the letter in the middle.
4. All letters can be used multiple times.
5. If the word is found in the dictionary, you're provided with its definition and the word is added to your word list.
