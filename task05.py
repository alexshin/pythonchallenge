import requests
import re

def get_body(start: str) -> str:
    source_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'.format(start)
    r = requests.get(source_url)
    number = re.findall('and the next nothing is ([0-9]+)', r.text)
    print(number)
    if len(number) > 0:
        print(r.text)
        get_body(number[0])
    else:
        print('Lucky, I found it! ')
        print(r.text)

#get_body('12345')
# second step
get_body('63579')