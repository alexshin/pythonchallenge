import requests
import zipfile
import io
import re


def find_in_file(num, archive, comments):
    t = archive.read('{0}.txt'.format(num)).decode('utf-8')
    match = re.match('Next nothing is (\d+)', t)
    if match != None:
        comments.append(archive.getinfo('{0}.txt'.format(num)).comment.decode('utf-8'))
        print(t)    
        find_in_file(match.group(1), archive, comments)
    else:
        print('Oh, lucky! I found it')
        print(t)

if __name__ == '__main__':
    r = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')
    start_with = '90052'

    archive = zipfile.ZipFile(io.BytesIO(r.content))

    comments = []
    find_in_file(start_with, archive, comments)

    print(''.join(comments))