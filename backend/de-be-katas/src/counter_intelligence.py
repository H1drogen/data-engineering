import string

def counter_intelligence(encrypted_str):
    difference = ord('X') - ord(encrypted_str[-1].upper())
    decrypted_str = ""
    for char in encrypted_str:
        if char.isalpha():
            char = chr(abs(ord(char.upper()) + difference - ord('A')) % 26 + ord('A'))
            decrypted_str += char
        else:
            decrypted_str += char
    return decrypted_str
