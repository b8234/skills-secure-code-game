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

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # Secure version: path traversal is checked before opening the file
    def get_prof_picture(self, path=None):
        if not path:
            return None

        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.abspath(os.path.join(base_dir, path))

        # secure check: is full path still under base_dir?
        if not full_path.startswith(base_dir):
            return None

        with open(full_path, 'rb') as pic:
            picture = bytearray(pic.read())
            self.prof_picture = picture

        return full_path

    # Secure version: path traversal is checked before opening the file
    def get_tax_form_attachment(self, path=None):
        if not path:
            raise Exception("Error: Tax form is required for all users")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.abspath(path)

        # secure check: is full path still under base_dir?
        if not full_path.startswith(base_dir):
            return None

        with open(full_path, 'rb') as form:
            tax_data = bytearray(form.read())
            self.tax_form_attachment = tax_data

        return full_path
