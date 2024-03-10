"""
Creator: Jordan Dexter
Date: March 6, 2024
Description: This web application is simple barcode scanner. The application uses flask as a minimalistic front-end
             and google cloud storage, and a barcode-generating api as a back-end. Data can be re-fetched in a new session
             via the session-key located in the top corner. 

             More information on the barcode api can be found here: https://barcodeapi.org/
                This is an open-source project which returns an barcode image containing the data entered.
"""


import flask, os
from sources.Index import Index
from sources.Submit import Submit
from sources.About import About

# Flask instance for front-end
app = flask.Flask(__name__)

# Home page
app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET', 'POST'])

# Handles the submission of data as well as the generation of the barcode image
app.add_url_rule('/submitted',
                 view_func=Submit.as_view('submit'),
                 methods=['GET', 'POST'])

# Contains information about this
app.add_url_rule('/about',
                 view_func=About.as_view('about'),
                 methods=["GET"])

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get('PORT',5000)))

