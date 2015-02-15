#!/usr/bin/env python3

"""
Simple little commandline tool for quickly uploading files
"""

import sys
import requests
import mimetypes
from envtools import basename

# Declare a few patterns and cosntants
server = 'http://localhost:8080'
upload_url = "{server}/upload".format(server=server)
download_url = "{server}/download/{{key}}".format(server=server)
result_row = '{download_url} :: {{filename}}'.format(download_url=download_url)


def upload(*paths):
    """
    This loops over a set of files and uploads them one by one. The result is then printed.
    """

    files = []
    for path in paths:
        filename = basename(path)
        filereader = open(path, 'rb')
        mimetype = mimetypes.guess_type(path)[0] or 'text/plain'
        files.append(('files', (filename, filereader, mimetype)))

    # Send everything to the server.
    result = requests.post(upload_url, files=files)

    # See if the server liked it.
    if result.status_code == 200:
        files = result.json()['response']
        for file in files:
            print(result_row.format(**file))
    else:
        # Something went wrong, let's see if the user can figure it out for me and write a patch :)
        print(result.text)


def async_upload(*paths):
    """
    This loops over a set of files and uploads them all at once. The result is then printed.
    """

    files = []
    for path in paths:
        filename = basename(path)
        filereader = open(path, 'rb')
        mimetype = mimetypes.guess_type(path)[0] or 'text/plain'
        files.append(('files', (filename, filereader, mimetype)))

    # Send everything to the server.
    result = requests.post(upload_url, files=files)

    # See if the server liked it.
    if result.status_code == 200:
        files = result.json()['response']
        for file in files:
            print(result_row.format(**file))
    else:
        # Something went wrong, let's see if the user can figure it out for me and write a patch :)
        print(result.text)


def main():
    files = sys.argv[1:]

    if not files:
        print('Usage: %s path [path ...]' % sys.argv[0])
        exit(1)

    upload(*files)


if __name__ == '__main__':
    main()
