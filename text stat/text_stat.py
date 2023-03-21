from collections import Counter
import re
import os


def open_file(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    else:
        return None


def count_paragraphs(filename):
    count = 0
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if line[:5] == "     ":
                count += 1

    return count


def get_words(file):
    raw_text = re.findall(r'\w+', file)
    words = [word.lower() for word in raw_text if word.isalpha()]

    return words


def get_all_letters(words):
    return ''.join(words).lower()


def word_freq(words, letter):
    counter = 0

    for word in words:
        if letter in word:
            counter += 1

    return counter / len(words)


def letter_stat(letters, words):
    letter_count = len(letters)
    stat = dict(Counter(letters))

    for key in stat.keys():
        letter_freq = stat[key] / letter_count
        word_proportion = word_freq(words, key)

        stat[key] = (letter_freq, word_proportion)

    return stat


def bilingual_count(words):
    count = 0

    for word in words:
        if re.search(r'[a-zA-Z]', word) and re.search(r'[а-яА-Я]', word):
            count += 1

    return count


def text_stat(filename):
    file = open_file(filename)
    if not file:
        return {"error": "No such file or directory"}

    else:
        words = get_words(file)
        letters = get_all_letters(words)

        stats = letter_stat(letters, words)
        stats["word_amount"] = len(words)
        stats["paragraph_amount"] = count_paragraphs(filename)
        stats["bilingual_word_amount"] = bilingual_count(words)

        return stats


filename = "./data/empty.txt"

print(text_stat(filename))
