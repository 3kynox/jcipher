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

def createCylinder(file, n):
    cylinder = open(file, "w")
    output = ''

    for line in range(n):
        output += mix()
        output += '\n'

    cylinder.write(output)
    cylinder.close()

#################### TEST AREA ####################

# Test function convertLetters()
#userInput = input('Enter your input: ')
#print(convertLetters(userInput))

# Test function createCylinder()
createCylinder('cylinder.txt', 26)

