import requests
import pickle

if __name__ == '__main__':
    r = requests.get('http://www.pythonchallenge.com/pc/def/banner.p')
    text = pickle.loads(bytes(r.text, 'utf-8'))
    for line in text:
        output = ''.join([segment[0] * segment[1] for segment in line])
        print(output)