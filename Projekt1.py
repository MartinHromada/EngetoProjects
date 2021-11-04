TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

         '''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

         '''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''']

separator = '-' * 40
regUsers = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

inptUssername = input('Ussername: ')
inptPassword = input('Password: ')

print(separator)

if inptPassword == regUsers.get(inptUssername):
    print(f"Welcome in app {inptUssername}.")
else:
    print(f"Ussername or Password is not correct.\n{separator}")
    exit()

print(f"We have {str(len(TEXTS))} texts to be analyzed.\n{separator}")

choice = input("Enter number btw. 1 and 3 to select: ")

if not choice.isnumeric():
    print(f"Entered symbol is not number! \nClosing...\n{separator}")
    exit()
elif int(choice) not in range(1, 4):
    print(f"Out of texts range.\nClosing...\n{separator}")
    exit()
else:
    analyzedText = TEXTS[int(choice) - 1].split()
    print(separator)

clearWords = []
for slovo in analyzedText:
    clearWord = slovo.strip(' ,.-§¨)?:_"!/(')
    if slovo in ' ,.-§¨)?:_"!/(':
        continue
    else:
        clearWords.append(clearWord)

countDict = {'word': len([word for word in clearWords]),
             'numm': len([word for word in clearWords if word.isnumeric()]),
             'low': len([word for word in clearWords if word.islower()]),
             'tit': len([word for word in clearWords if word.istitle()]),
             'upp': len([word for word in clearWords if word.isupper() and word.isalpha()]),
             'nummSum': sum([int(word) for word in clearWords if word.isnumeric()])
             }

wordsLen = {}

for word in clearWords:
    if len(word) not in wordsLen.keys():
        wordsLen.setdefault(len(word), 1)
    else:
        wordsLen[len(word)] += 1

print(f"""There are {countDict.get('word')} in selected text.
There are {countDict.get('tit')} titlecase words.
There are {countDict.get('upp')} uppercase words.
There are {countDict.get('low')} lowercase words.
There are {countDict.get('numm')} numeric words.
The summ of all the numbers is {countDict.get('nummSum')}.""")

print(separator)

jG1 = len(str(sorted(wordsLen.keys(), reverse=True)[0])) + 1
jG2 = sorted(wordsLen.values(), reverse=True)[0] + 1

print(f"{'LEN'.rjust(jG1)}|{'OCCURENCES'.center(jG2)}{'|Nr.'.ljust(jG2 - len('OCCURENCES'))}\n{separator}")

for i in sorted(wordsLen.keys()):
    print(f"{str(i).rjust(jG1)}|{'*' * wordsLen.get(i)}{'|'.rjust(jG2 + 1 - wordsLen.get(i))}{str(wordsLen.get(i))}")

print(separator)
