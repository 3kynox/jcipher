import collections, string, random

# Take a text and format it without spaces, accents and special chars
def convertLetters(text):
    table = collections.defaultdict(lambda: None)
    table.update({
        ord('é'):'e', ord('ë'):'e', ord('é'):'e', ord('è'):'e',
        ord('ô'):'o', ord('ö'):'o', ord('ò'):'o', ord(' '):'',
        ord('â'):'a', ord('ä'):'a', ord('à'):'a', ord('à'):'a',
        ord('û'):'u', ord('ü'):'u', ord('ù'):'u', ord('ç'):'c',
        })
    table.update(dict(zip(map(ord,string.ascii_uppercase), string.ascii_lowercase)))
    table.update(dict(zip(map(ord,string.ascii_lowercase), string.ascii_lowercase)))
    table.update(dict(zip(map(ord,string.digits), string.digits)))
    
    return text.translate(table,)

# Takes alphabet letters and return it uppercase shuffled
def mix():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = random.sample(alphabet, len(alphabet))

    return ''.join(alphabet).upper()

# Generate a file with n lines of mix() function
def createCylinder(file, n):
    cylinder = open(file, "w")
    output = ''

    for line in range(n):
        output += mix()
        output += '\n'

    cylinder.write(output)
    cylinder.close()

# Return a dictionary from createCylinder file content
def loadCylinder(file):
    dict = {}
    i = 1
    
    try:
        with open(file, 'r') as openfile:
            for line in openfile:
                dict[i] = line.rstrip()
                i += 1
            openfile.close()
            return dict
    except:
        return "The file does not exists!"

# Check if there is n elements in key list
# and if elements from 1 to n exists in key list
def keyOK(key, n):
    if len(key) == n:
        for i in range(1, n + 1):
            if i in key:
                continue
            else:
                return False
        return True
    else:
        return False
    
# Returns int list of n shuffled elements
def createKey(n):
    return random.sample(range(1, n + 1), n)

# Find index of letter parameter in a list
def find(letter, alphabet):
    for i in range(len(alphabet)):
        if letter == alphabet[i]:
            return i

# Return modulo [26] of (i + 6)
def shift(i):
    return (i + 6) % 26

# Return letter + index of 6 in a circular way from a list
def cipherLetter(letter, alphabet):
    return alphabet[shift(find(letter, alphabet))]

# Returns encrypted string according to a keyList and cylinderList
def cipherText(cylinder, key, text):
    encryptedText = ''
    
    if keyOK(key, len(cylinder)):
        text = convertLetters(text)
        
        for i, c in enumerate(text):
            encryptedText += cipherLetter(c.upper(), cylinder[key[i]])
        return encryptedText
    else:
        return 'Error: Invalid key !'

#################### UN-CRYPT ####################
def unShift(i):
    return (i - 6) % 26

def unCipherLetter(letter, alphabet):
    return alphabet[unShift(find(letter, alphabet))]

def unCipherText(cylinder, key, text):
    unCryptedText = ''
    
    if keyOK(key, len(cylinder)):
        for i, c in enumerate(text):
            unCryptedText += unCipherLetter(c, cylinder[key[i]])
        return unCryptedText
    else:
        return 'Error: Invalid key !'
    
#################### TEST AREA ####################
# Test function cipherText()
#createCylinder('cylinder.txt', 10)
cylinder = loadCylinder('MP-1ARI.txt')
#key = createKey(10)
key = [12, 16, 29, 6, 33, 9, 22, 15, 20, 3, 1, 30, 32, 36, 19, 10, 35, 27, 25, 26, 2, 18, 31, 14, 34, 17, 23, 7, 8, 21, 4, 13, 11, 24, 28, 5]
print(unCipherText(cylinder, key, "GRMYSGBOAAMQGDPEYVWLDFDQQQZXXVMSZFSE"))



