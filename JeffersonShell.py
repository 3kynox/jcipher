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
    if letter.isupper():
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                return i
    else:
        return 'Error: The first parameter must be an uppercase letter !'

# Return modulo [26] of (i + 6)
def shift(i):
    return (i + 6) % 26

# Return letter + index of 6 in a circular way
def cipherLetter(letter, alphabet):
    if letter.isupper():
        for i in range(len(alphabet)):
            if letter == alphabet[i]:
                i = i + 6
                if i > 25:
                    i = i - 26
                return alphabet[i]
    else:
        return 'Error: The first parameter must be an uppercase letter !'

#################### TEST AREA ####################

# Test function convertLetters()
#userInput = input('Enter your input: ')
#print(convertLetters(userInput))

# Test function createCylinder()
#createCylinder('cylinder.txt', 26)

# Test function loadCylinder()
#print(loadCylinder('cylinderr.txt'))

# Test keyOK() - createKey()
#myList = createKey(11)
#print(keyOK(myList, 11))

# Test function find()
#print(find('L', mix()))

# Test function shift()
#print(shift(12))

# Test function cipherLetter()
print(cipherLetter('L', mix()))
