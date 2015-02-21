
Hi, this will probably be filled in better later. Bear with me.

Dependencies:

Python3
Flask
...Anything else?


You need to make a settings.ini:

Example:
    \[DEFAULT\]
    download_redirect_url = https://127.0.0.1/files/\{key\}
    upload_path = /tmp/upload/
    max_file_size = 52428800
    max_request_size = 524288000


Explanation:
"upload_path"               Where uploaded files are stored

"download_redirect_url"     Point this to a webserver that's actually good at service static content.
                            The URL should contain "{key}", which whill be replaced with the key for the
                            file you wish to download. This is handled dynamically by the API.

"max_file_size"             The maximum size for any given file.

"max_request_size"          The maximum size for the request containing all the files.