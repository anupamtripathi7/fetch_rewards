import string
import json
import nltk
nltk.download('punkt')


def read_text(filename):
    with open(filename, 'r', encoding='utf8') as f:
        x = f.readlines()
    return x


def save_json(data):
    with open('word_count.json', 'w') as fp:
        json.dump(data, fp)


def save_text(filename, x):
    x = ''.join(x)
    with open(filename, 'w', encoding='utf8') as f:
        f.write(x)


def tokenize(x):
    new_sent = []
    for sent in x:
        new_sent.extend(nltk.sent_tokenize(sent, 'english') + ['\n'])
    return new_sent


def remove_punctuations(s):
    table = str.maketrans(dict.fromkeys(string.punctuation))
    s = s.translate(table)
    return s
