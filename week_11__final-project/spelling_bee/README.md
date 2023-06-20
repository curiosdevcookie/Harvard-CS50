# Urban Spelling Bee

We love playing the [Spelling Bee of the NY Times](https://www.nytimes.com/puzzles/spelling-bee).

So I thaught that this would make a fun challenge for me to implement. To give it a little spin, this is Spelling Bee with the Urban Dictionary as its lexicon.

Also, as we aren't English native speakers, the player is provided with the definition of the word if the word is found in the dictionary.

_Protip_: Click on the bee to get a new set of letters!

## How to play

The game is played as follows:

1. Create as many words as you can by clicking on the given letters.
2. The word must be at least 4 letters long.
3. The word must contain the letter in the middle.
4. All letters can be used multiple times.
5. If the word is found in the dictionary, you're provided with its definition and the word is added to your word list.

## How to run the app, choose:

- [Run the app locally](#run-the-app-locally)
  - [Installation](#installation)
  - [Set up the database](#set-up-the-database)
  - [Configuration](#configuration)
  - [Run the app](#run-the-app)
- [Run the app via Docker](#run-the-app-via-docker)
  - [Installation](#installation-1)
  - [Run the app](#run-the-app-1)

## Run the app locally

### Installation

To install the game, you need to install the required packages via your terminal. You can do this by running

```bash
pip install -r requirements.txt
```

### Set up the database

To install the database, you need to run the following command in your terminal:

```bash
wget "https://dl.dropboxusercontent.com/s/ooctnlclt9bdmeu/dictionary.db" -O dictionary.db
```

### Configuration

In your `app.py` file, set the `is_local` variable to `True`:

```python
is_local = True
```

This is important for the app to choose the correct path to the database.

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

### Run the app

Run the following command in your terminal to run the container:

```bash
docker run -p 8000:8000 -v "$(pwd)/data:/data" spelling-bee
```

The `$(pwd)/data:/data` part in the docker run command is used to mount the  data directory to the /data directory inside the Docker container. This allows the container to access the dictionary.db.

You can now access the app on `http://127.0.0.1:8000/`.
