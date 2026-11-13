alphabet_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabet_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Function to filter out letters from a string not in a certain alphabet

def filter(text: str, include_if: list) -> str:
    clean_text = ""

    for char in text:
        if char in include_if:
            clean_text += char

    return clean_text

# Function to turn text into a list of 'collumns' of a certain length

def collumnise(text: str, key_length: int) -> list:
    collumnate = text

    collumns = []
    block = ""

    for char in collumnate:
        block += char
        if len(block) == key_length:
            collumns.append(block)
            block = ""

    return collumns

def generate_key_alphabet(keyword: str, cont_from_key: bool = True, alphabet: list = alphabet_upper) -> str:
    key_alphabet = ""
    
    for char in keyword:
        if char in alphabet:
            if (char in key_alphabet):
                pass
            else:    
                key_alphabet += (char)
        else:
            raise ValueError(f"The letter {char} from the keyword is not in the selected alphabet.")

    if cont_from_key == True:
        reordered_alphabet = alphabet[alphabet.index(key_alphabet[len(key_alphabet) - 1]) + 1 : len(alphabet)] + alphabet[0 : alphabet.index(key_alphabet[len(key_alphabet) - 1]) + 1]
    else:
        reordered_alphabet = alphabet

    for char in reordered_alphabet:
        if char in key_alphabet:
            pass
        else:
            key_alphabet += (char)

    return key_alphabet

def list_to_string(list_in: list) -> str:
    string_out = ""

    for char in list_in:
        string_out += char

    return string_out

def string_to_list(string_in: str) -> list:
    list_out = []

    for char in string_in:
        list_out.append(char)

    return list_out

def bigram_frequencies(cipher_text: str):
    cipher_text_list = string_to_list(cipher_text)
    bigrams = []

    for bg_index in range (0, round(len(cipher_text) / 4) - 1):
        bigram = ""

        bigram += cipher_text_list[2 * bg_index - 2]
        bigram += cipher_text_list[2 * bg_index - 1]

        bigrams.append(bigram)

    bigram_freqs = {}

    for bigram in bigrams:
        if bigram in bigram_freqs:
            bigram_freqs[bigram] += 1
        else:
            bigram_freqs[len(bigram_freqs)] = {bigram: 1}

    return bigram_freqs

def flip(text: str) -> str:
    text_flipped = []

    for char in string_to_list(text):
        text_flipped.insert(0, char)

    return list_to_string(text_flipped)