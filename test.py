"""
Silly test tool for uploading some junk to the API
"""

import requests


url = 'http://127.0.0.1:5000/upload'

files = [('files', ('important1.txt', b'important datas', 'text/plain')),
         ('files', ('important2.txt', b'more important datas', 'text/plain')),
         ('files', ('dumbfile.txt', b'a' * 1024, 'text/plain'))]

response = requests.post(url, files=files)
print(response.text)