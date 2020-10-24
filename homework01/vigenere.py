def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
     Encrypts plaintext using a Vigenere cipher.

     >>> encrypt_vigenere("PYTHON", "A")
     'PYTHON'
     >>> encrypt_vigenere("python", "a")
     'python'
     >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
     'LXFOPVEFRNHR'
     """
    ciphertext = ""
    for sn in range(len(plaintext)):
        ltr = plaintext[sn]
        keyword = keyword.upper()
        shift = ord(keyword[sn % len(keyword)]) - 65
        sn = 0
        if ltr.islower():
            ciphertext += chr(97 + ((ord(ltr) - 97 + shift) % 26))
        elif ltr.isupper():
            ciphertext += chr(65 + ((ord(ltr) - 65 + shift) % 26))
        else:
            ciphertext += ltr
        sn += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for sn in range(len(ciphertext)):
        ltr = plaintext[sn]
        keyword = keyword.upper()
        shift = ord(keyword[sn % len(keyword)]) - 65
        sn = 0
        if ltr.islower():
            plaintext += chr(97 + ((ord(ltr) - 97 - shift) % 26))
        elif ltr.isupper():
            plaintext += chr(65 + ((ord(ltr) - 65 - shift) % 26))
        else:
            plaintext += ltr
        sn += 1
    return plaintext
