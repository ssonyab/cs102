import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    text = list(plaintext)
    for i in text:
        i = ord(i)
        if i >= ord('a') and i <= ord('z') or i >= ord('A') and i <= ord('Z'):
            if i > ord('z') - shift and i <= ord('z'):
                i -= 26
            elif i > ord('Z') - shift and i <= ord('Z'):
                i -= 26
            i += shift
            i = chr(i)
            ciphertext += i
        else:
            i = chr(i)
            ciphertext += i
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
      Decrypts a ciphertext using a Caesar cipher.

      >>> decrypt_caesar("SBWKRQ")
      'PYTHON'
      >>> decrypt_caesar("sbwkrq")
      'python'
      >>> decrypt_caesar("Sbwkrq3.6")
      'Python3.6'
      >>> decrypt_caesar("")
      ''
      """
    plaintext = ""
    text = list(ciphertext)
    for i in text:
        i = ord(i)
        if i >= ord('a') and i <= ord('z') or i >= ord('A') and i <= ord('Z'):
            if i < ord('a') + shift and i >= ord('a'):
                i += 26
            elif i < ord('A') + shift and i >= ord('A'):
                i += 26
            i -= shift
            i = chr(i)
            plaintext += i
        else:
            i = chr(i)
            plaintext += i
    return plaintext

def caesar_breaker(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
           >>> d = {"python", "java", "ruby"}
           >>> caesar_breaker("python", d)
           0
           >>> caesar_breaker("sbwkrq", d)
           3
    """
    best_shift = 0
    text = list(ciphertext.lower())
    for i in dictionary:
        el = list(i)
        sh1 = ord(text[0]) - ord(el[0])
        sh2 = ord(text[1]) - ord(el[1])
        if sh1 < 0:
            sh1 += 26
        if sh2 < 0:
            sh2 += 26
        if sh1 == sh2:
            best_shift = sh1
    return best_shift


