from werkzeug.utils import redirect
import settings

from glob import glob
from flask import Flask
from uploadhelper import handle_file_uploads


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = settings.get_setting('max_request_size')


@app.route('/')
@app.route('/download/')
def index():
    """
    Placeholder, lists all files in upload_path for now.
    It should show us a nice landing page, probably with a bunch of crap on it that makes uploading stuff easier.
    """
    files = glob(settings.get_setting('upload_path') + '/*')
    return '<br />'.join(files)


@app.route('/upload', methods=('GET', 'POST'))
def upload():
    """
    Handle file uploads.
    """
    return handle_file_uploads()


@app.route('/download/<string:key>')
def download(key):
    """
    What we should do here is redirect the client to another webserver like nginx or lighttpd,
    which would then serve the actual file.
    """

    download_redirect_url = settings.get_setting("download_redirect_url")
    return redirect(download_redirect_url.format(key=key))


if __name__ == '__main__':
    app.run(debug=True)