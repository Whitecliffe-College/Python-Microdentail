# compute a Caesar cipher on a plain text
def caesar_cipher(text, key):
    # make a string to hold the encrypted text
    encrypted_string = ""
    # go through each character in the text
    for c in text:
        # if it's not a letter, leave it as it is
        if not c.isalpha():
            encrypted_string += c
        # otherwise, encrypt it with the caesar cipher
        else:
            # get the unicode point of the character
            c_unicode = ord(c)
            # get the unicode point of the encrypted character
            c_unicode = ((c_unicode - ord("a") + key) % 26) + ord("a")
            # convert the encrypted unicode point back to a character
            encrypted_string += chr(c_unicode)
    # return the encrypted string
    return encrypted_string


# write unit test for the caesar cipher function
def test_caesar_cipher_without_whitespace():
    assert caesar_cipher("abc", 1) == "bcd"

def test_caesar_cipher_with_whitespace():
    assert caesar_cipher("abcd xyz", 4) == "efgh bcd"


def test_caesar_cipher_with_punctuation():
    assert caesar_cipher("abcd xyz!", 4) == "efgh bcd!"
    assert caesar_cipher("tjw,fhr", 3) == "wmz,iku"