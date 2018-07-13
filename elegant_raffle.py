import urllib.request
import json
import itertools
import random
import time
import sys
import numpy as np

url = ('https://api.github.com/repos/elegant-scipy/elegant-scipy'
       '/issues/308/comments?page={}')

comments = []

for page in itertools.count(1):
    print(f'Downloading comment page {page}')

    request = urllib.request.urlopen(url.format(page))
    response = json.load(request)

    if not response:
        break
    else:
        comments.extend(response)

authors = ['stefanv', 'jni', 'hdashnow']
commenters = [comment['user']['login'] for comment in comments]
commenters = [commenter for commenter in commenters
              if not any((commenter == author) for author in authors)]

commenters = np.unique(list(commenters))  # you didn't think you could sneak
                                          # another ticket in there, did you? ;)


def typewrite(text, delay=0.2, after_delay=0.3):
    for ch in text:
        print(ch, end='')
        time.sleep(random.random() * delay)
        sys.stdout.flush()

    print('')
    time.sleep(after_delay)


typewrite('\n\nGet ready for the SciPy 2017 Elegant SciPy raffle...\n')
typewrite('OK...\n')
typewrite('Are you ready?\n')
typewrite('Good.\n')
typewrite('Hold on, let me get my hat.\n')
typewrite('OK, add your tickets into the hat.\n')
typewrite(f'It looks like we received... {len(commenters)} entries.\n')
typewrite('And, our winners, drawn with random seed "scipy2017", are:\n\n\n')

random.seed("scipy2017")
random.shuffle(commenters)

for n, potential_winner in enumerate(commenters):
    typewrite(f'\n{n + 1} {potential_winner}\n')
    input('moar?! ')
