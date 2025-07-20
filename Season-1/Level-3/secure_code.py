# Welcome to Secure Code Game Season-1/Level-3!

# You know how to play by now, good luck!

import os
from flask import Flask, request

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

class TaxPayer:

    SAFE_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    def _resolve_safe_path(self, relative_path):
        """Resolves path within SAFE_ROOT and validates it doesn't escape."""
        if not relative_path:
            return None

        normalized = os.path.normpath(relative_path)

        # Reject absolute paths or traversal
        if os.path.isabs(normalized) or normalized.startswith('..'):
            return None

        full_path = os.path.abspath(os.path.join(self.SAFE_ROOT, normalized))

        if not full_path.startswith(self.SAFE_ROOT):
            return None

        return full_path

    # returns the path of an optional profile picture that users can set
    def get_prof_picture(self, path=None):
        resolved = self._resolve_safe_path(path)
        if not resolved or not os.path.isfile(resolved):
            return None

        with open(resolved, 'rb') as pic:
            picture = bytearray(pic.read())
            self.prof_picture = picture

        return resolved

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        resolved = self._resolve_safe_path(path)
        if not resolved or not os.path.isfile(resolved):
            raise Exception("Invalid or missing tax form file")

        with open(resolved, 'rb') as form:
            tax_data = bytearray(form.read())
            self.tax_form_attachment = tax_data

        return resolved
