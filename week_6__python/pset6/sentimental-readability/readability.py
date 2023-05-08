def main():

    user_input = get_user_input()
    letters = count_letters(user_input)
    words = count_words(user_input)
    sentences = count_sentences(user_input)
    cli = coleman_liau_index(letters, words, sentences)
    print_result(cli)
    

def get_user_input():
    user_input = input("Text: ")
    return user_input


def count_letters(user_input):
    letters = filter(str.isalpha, user_input)
    letters = len(list(letters))
    print(letters)
    return letters


def count_words(user_input):
    words = user_input.split(" ")
    words = len(words)
    print(words)
    return words


def count_sentences(user_input):
    sentences = 0
    for i in range(len(user_input)):
        if user_input[i] == '.' or user_input[i] == '!' or user_input[i] == '?':
            sentences += 1
        elif user_input[i] == ',' or user_input[i] == ';' or user_input[i] == ':':
            continue
    print(sentences)
    return sentences


def coleman_liau_index(letters, words, sentences):
    L = letters * 100 / words
    S = sentences * 100 / words
    index = round(0.0588 * L - 0.296 * S - 15.8)
    return index


def print_result(cli):
    if cli < 1:
        print("Before Grade 1")
    elif cli >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {cli}")


main()

