# Define caeser encrypt

def caesar_enc(plain_text: str, shift: int, alphabet: list) -> str:
    try:
        encrypt_text = ""

        for char in plain_text:
            enc_char_index = (alphabet.index(char) + shift) % len(alphabet)
            encrypt_text += alphabet[enc_char_index]

        return encrypt_text
    except:
        raise ValueError("Characters in plain text not in alphabet")

# Define caeser decrypt

def caesar_dec(cipher_text: str, shift: int, alphabet: list) -> str:
    try:
        decrypt_text = ""

        for char in cipher_text:
            dec_char_index = (alphabet.index(char) - shift) % len(alphabet)
            decrypt_text += alphabet[dec_char_index]

        return decrypt_text
    except:
        raise ValueError("Characters in cipher text not in alphabet")