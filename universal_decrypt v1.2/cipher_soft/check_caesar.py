import caesar_cipher

default_crib = "MYDEAR"
default_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Define function to check if a given text has likely been encoded with a caesar cipher

def check(cipher_text: str, crib: str = default_crib, crib_start: bool = True, alphabet: list = default_alphabet) -> bool:
    # Find what text to check against the crib
    
    if crib_start == True:
        ct_sample = cipher_text[0:len(crib)]
    else:
        ct_sample = cipher_text[len(cipher_text) - len(crib):len(cipher_text)]

    # Run through all caesar shifts

    is_caesar = False

    for shift in range(0, len(alphabet)):
        if caesar_cipher.caesar_dec(ct_sample, shift, alphabet) == crib:
            is_caesar = True

    return is_caesar