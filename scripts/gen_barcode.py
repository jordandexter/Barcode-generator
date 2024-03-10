"""
Name: Jordan Dexter
Date: March 6, 2024
Desc: This file defines the function responsible for making the api call to barcode api and writing the data recieved to a
      temporary file.
      
      def gen_barcode(): makes a call to the api which responds with the the image and writes the data to a file, if possible.
"""

import requests

def gen_barcode(input):
    s = requests.session()

    response = s.get("https://barcodeapi.org/api/" + input, stream=True)

    filename = input + ".png"

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response:
                f.write(chunk)
    else:
        return False
    
    return True
    
    

