def word_count (book):
    words = book.split()
    total_words = len(words)
    return total_words

def character_count (book):
    book = book.lower()
    characters = {}
    splitted = list(book)
    for character in splitted:
        if character not in characters:
            characters[character] = 1
        else:
            characters[character] += 1
    return characters

def sort_on(d):
    return d["num"]


def sorted(characters):
    sorted_list = []
    for character in characters:
        sorted_list.append({"char": character, "num": characters[character]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list