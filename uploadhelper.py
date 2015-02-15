import os
from werkzeug.utils import secure_filename
import settings
import hashlib

from apiresponse import APIResponse
from flask import request


def _generate_key(data):
    """
    Generates a key for the file. Temporary solution, we can do better by
    querying a database for the next ID and translating it to letters or something.
    """
    return hashlib.sha1(data).hexdigest()


def _clean_filename(filename):
    """
    Temporary solution, will replace with a checksum of the file content instead
    """
    return secure_filename(filename)


def handle_file_uploads():
    """
    Handles multiple uploads
    """

    try:
        files = request.files.getlist("files")
        upload_path = settings.get_setting('upload_path')
        max_file_size = settings.get_setting('max_file_size')

        # We'll be preparing a response for the client.
        # The filename is what we'll say the file is called to any clients downloading it.
        # The key is what we'll store it as on our system, and what a client will specify when they want a file.
        # Format is [{"filename": filename, "key": key}, ...]
        response = []

        for file in files:
            # We'll be storing this original filename somewhere.
            original_filename = file.filename

            # This is the filename we'll report back to the browser.
            # Anyone who downloads it gets this name.
            clean_filename = _clean_filename(original_filename)

            # Hijack the data so we can checksum it.
            data = file.read()

            # Make sure the data is <= max_file_size
            if len(data) > max_file_size:
                message = 'A file was too big. Max size is %d bytes, the file was %d.'
                raise Exception(message % (max_file_size, len(data)))

            # Generate the checksum.
            key = _generate_key(data)

            # Figure out where to store it.
            destination = os.path.join(upload_path, key)

            # Store the data, but only if we don't already have it.
            # What can happen here is that we have multiple filenames pointing to the same file.
            # This shouldn't be a problem for us.
            if not os.path.isfile(destination):
                with open(destination, 'wb+') as outfile:
                    outfile.write(data)

            # Add this file to the response
            response.append({"filename": clean_filename, "key": key})

        #
        # TODO: Everything went right, so add these files to the database
        #

        # Everything went right, so let's shovel stuff right back
        return str(APIResponse(response))

    except Exception as exception:
        # Shit has hit the fan. Let's tell the client what we know.
        return str(APIResponse(exception=exception, success=False))
