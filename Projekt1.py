from string import punctuation as pun

TEXTS = [
    '''Situated about 10 miles west of Kemmerer, 
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
garpike and stingray are also present.'''
]

SEPARATOR = '-' * 40
REG_USSERS = {'bob': '123', 'ann': 'pass123', 'mike': 'password123',
              'liz': 'pass123'}

inpt_ussername = input('Ussername: ')
inpt_password = input('Password: ')

print(SEPARATOR)

if inpt_password == REG_USSERS.get(inpt_ussername):
    print(f"Welcome in app {inpt_ussername}.")
else:
    print(f"Ussername or Password is not correct.\n{SEPARATOR}")
    exit()

print(f"We have {str(len(TEXTS))} texts to be analyzed.\n{SEPARATOR}")

choice = input("Enter number btw. 1 and 3 to select: ")

if not choice.isnumeric():
    print(f"Entered symbol is not number! \nClosing...\n{SEPARATOR}")
    exit()
elif int(choice) not in range(1, len(TEXTS) + 1):
    print(f"Out of texts range.\nClosing...\n{SEPARATOR}")
    exit()
else:
    clear_words = [slovo.strip(pun) for slovo in TEXTS[int(choice) - 1].split()
                   if slovo.strip(pun) != '']

print(SEPARATOR)

count_dict = {'word': len([word for word in clear_words]),
              'numm': len([word for word in clear_words if word.isnumeric()]),
              'low': len([word for word in clear_words if word.islower()]),
              'tit': len([word for word in clear_words if word.istitle()]),
              'upp': len([word for word in clear_words
                          if word.isupper() and word.isalpha()]),
              'nummSum': sum([int(word) for word in clear_words
                              if word.isnumeric()])
              }

words_len = {}

for word in clear_words:
    if len(word) not in words_len.keys():
        words_len.setdefault(len(word), 1)
    else:
        words_len[len(word)] += 1

print(f"""There are {count_dict.get('word')} in selected text.
There are {count_dict.get('tit')} titlecase words.
There are {count_dict.get('upp')} uppercase words.
There are {count_dict.get('low')} lowercase words.
There are {count_dict.get('numm')} numeric words.
The summ of all the numbers is {count_dict.get('nummSum')}.""")

print(SEPARATOR)

jg1 = len(str(sorted(words_len.keys(), reverse=True)[0])) + 1
jg2 = sorted(words_len.values(), reverse=True)[0] + 1

print(f"{'LEN'.rjust(jg1)}|{'OCCURENCES'.center(jg2)}"
      f"{'|Nr.'.ljust(jg2 - len('OCCURENCES'))}\n{SEPARATOR}")

for i in sorted(words_len.keys()):
    print(f"{str(i).rjust(jg1)}|{'*' * words_len.get(i)}"
          f"{'|'.rjust(jg2 + 1 - words_len.get(i))}{str(words_len.get(i))}")

print(SEPARATOR)
