"""
Name: Jordan Dexter
Date: March 6, 2024
Desc: This file defines the implemenation of the backend of the application. This application uses
      a google cloud storage bucket to hold previously generated images. 
"""

from google.cloud import storage
from scripts import gen_barcode
from IPython.display import Image
import os

class model():
    def __init__(self):
        # Initializes the storage client by project id, and initializes specified bucket.
        self.client = storage.Client('cloud-dexter-jodexter')
        self.bucket = self.client.get_bucket('barcode-images-jodexter')

    def select(self, val):
        # Specifies the bucket from which to select

        try:
            blob = self.bucket.get_blob(val)
        except:
            blob = "no image by that value"
            return blob
        
        blob.download_to_filename("tmp.png")
        os.rename("tmp.png", "static/tmp.png")
        return blob

    def insert(self, val):
        # Within the bucket, val become the name of the entry. 
        blob = self.bucket.blob(val)

        # Creates the file barcode image and stores it in the 'static' folder
        gen_barcode.gen_barcode(val)
        blob.upload_from_filename(val + ".png")

        os.remove(val + ".png")
        return True