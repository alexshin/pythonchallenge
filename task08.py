import requests
import io
import re
from PIL import Image


if __name__ == '__main__':
    r = requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png')
    p = Image.open(io.BytesIO(r.content))

    row = [p.getpixel((x, p.height / 2)) for x in range(p.width)]
    row = row[::7]

    ords = [r for r, g, b, a in row if r == g == b]

    hint = ''.join(map(chr, ords))
    print(hint)
    m = re.search('\[(.+)\]', hint)
    if m != None:
        print(''.join(map(chr, [int(x) for x in m.group(1).split(', ')])))