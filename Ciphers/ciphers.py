# ----------------------Index Sub Cipher----------------------


def encryptIndexSubstitutionCipher(text):
    encryptText = ""  # initialize return variable
    iterator = 0  # initialize iterator

    for char in text:
        temp = ord(char) - 96  # since all chars are lower, ord(a) - 96 would be 1
        if (temp >= 10):
            cipher = ""
            if (iterator > 0):  # space management
                cipher += " "
            cipher += str(temp)
            encryptText += cipher
        else:
            cipher = ""
            if (iterator > 0):
                cipher += " "
            cipher += "0"  # if number is less than 10 write zero behind
            cipher += str(temp)  # parse to string and save
            encryptText += cipher
        iterator += 1

    return encryptText


def decryptIndexSubstitutionCipher(text):
    decryptText = ""
    text = text.replace(" ", "")  # remove all spaces

    for index in range(0, len(text), 2):
        temp = text[index] + text[index + 1]  # check every 2 digits
        num = int(temp)  # parse to int and then get a letter
        decryptText += chr(num + 96)

    return decryptText


# ----------------------Morse Code----------------------
morseCode = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..'
}


def encryptMorseCode(text):
    encryptText = ""

    for char in range(0, len(text)):
        temp = ""
        if (char > 0):
            temp += " "  # space management
        temp += morseCode.get(text[char])  # get corresponding value for current key
        encryptText += temp

    return encryptText


def decryptMorseCode(text):
    decryptText = ""

    reverseMorse = {}

    for key, value in morseCode.items():
        reverseMorse[value] = key  # reverse values and keys
    temp = ""
    for index in range(0, len(text)):
        if (text[index] == " "):
            decryptText += reverseMorse.get(temp)  # if space is coming, this means end of the word
            temp = ""
        elif (index == len(text) - 1):
            temp += text[index]
            decryptText += reverseMorse.get(temp)  # if current char is last, end the word
        else:
            temp += text[index]

    return decryptText


# ----------------------Affine Cipher----------------------
def encryptAffineCipher(text, a, b):
    encryptText = ""

    for index in range(0, len(text)):
        order = ord(text[index]) - 97
        encryptText += chr((a * order + b) % 26 + 97)  # use the formula on ascii table

    return encryptText


def decryptAffineCipher(text, a, b):
    decryptText = ""

    for index in range(len(text)):
        order = ord(text[index]) - 97
        decryptText += chr((pow(a, -1, 26) * (order - b)) % 26 + 97)  # use the given formula

    return decryptText


# ----------------------Caesar Cipher----------------------
def encryptCaesarCipher(text, key1, key2):
    encrypted = ""

    i = 0

    for c in text:
        if i % 2 == 0:
            key = key1
        else:
            key = key2

        i += 1

        if c.isupper():  # check if it's an uppercase character

            newIndex = ord(c) - ord('A')

            # shift the current character by key positions
            shiftIndex = (newIndex + key) % 26 + ord('A')

            newChar = chr(shiftIndex)

            encrypted += newChar

        elif c.islower():  # check if its a lowecase character

            newIndex = ord(c) - ord('a')

            # shift the current character by key positions
            shiftIndex = (newIndex + key) % 26 + ord('a')

            newChar = chr(shiftIndex)

            encrypted += newChar

        elif c.isdigit():

            # if it's a number,shift its actual value
            newChar = (int(c) + key) % 10

            encrypted += str(newChar)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            encrypted += c

    return encrypted


# The Decryption Function
def decryptCaesarCipher(text, key1, key2):
    decrypted = ""

    i = 0

    for c in text:

        if i % 2 == 0:
            key = key1
        else:
            key = key2

        i += 1
        if c.isupper():

            newIndex = ord(c) - ord('A')

            # shift the current character by key positions
            shiftIndex = (newIndex - key) % 26 + ord('A')

            originalChar = chr(shiftIndex)

            decrypted += originalChar


        elif c.islower():

            newIndex = ord(c) - ord('a')

            # shift the current character by key positions
            shiftIndex = (newIndex - key) % 26 + ord('a')

            originalChar = chr(shiftIndex)

            decrypted += originalChar


        elif c.isdigit():

            # if it's a number,shift its actual value
            originalChar = (int(c) - key) % 10

            decrypted += str(originalChar)

        else:

            # if its neither alphabetical nor a number, just leave it like that
            decrypted += c

    return decrypted


# ----------------------Transposition Cipher----------------------
def encryptTranspositionCipher(text, key):
    encryptText = ""

    chunks = [text[i:i + key] for i in range(0, len(text), key)]  # make text divide into key-long chunks

    for i in range(key):
        for word in chunks:
            if (len(word) > i):
                encryptText += word[i]  # while possible add letters from the row

    return encryptText


def decryptTranspositionCipher(text, key):
    decryptText = ""

    lastlen = len(text) % key

    newKey = len(text) // key + 1 if (len(text) / key > len(text) // key) else len(
        text) // key  # New key should be equal to how many chunks we have

    chunks = []

    counter = 0

    if (lastlen != 0 and key <= len(text)):  # if there is short word
        checker = 0
        tracker = 0
        for i in range(0, len(text), newKey):  # while short word is not over, add by newKey
            chunks.append("")
            for j in range(i, i + newKey):
                chunks[counter] += text[j]

            counter += 1
            checker += 1

            if checker >= lastlen:
                tracker = i
                break

        for i in range(tracker + newKey, len(text), newKey - 1):  # when short word is over, add by newKey - 1
            chunks.append("")
            for j in range(i, i + (newKey - 1)):
                chunks[counter] += text[j]

            counter += 1

    else:
        chunks = [text[i:i + newKey] for i in
                  range(0, len(text), newKey)]  # if there is no short word, do as encrypt, but with new key

    for i in range(newKey):
        for word in chunks:
            if len(word) > i:
                decryptText += word[i]

    return decryptText
