import json


class APIResponse:
    """
    Container for a boolean success flag, an exception,
    and a response object that could be just about anything.
    Has the power of translating itself into json.
    """

    def __init__(self, response=None, success=True, exception=None):
        self._response = response
        self._success = success
        self._exception = exception

    def __str__(self):
        """
        If you use str() on an APIResponse, you get the jsonified data back.

        >>> apiresponse = APIResponse("Pls respond")
        >>> str(apiresponse)
        {"response": "Pls respond", "exception": "None", "success": true}
        """
        return json.dumps({'response': self._response,
                           'success': self._success,
                           'exception': str(self._exception)})

    @property
    def exception(self):
        return self._exception

    @exception.setter
    def exception(self, value):
        self._exception = value

    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, value):
        self._success = value

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value
