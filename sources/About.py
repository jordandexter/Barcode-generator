"""
Name: Jordan Dexter
Date: March 6, 2024
Desc: This file defines the methods for the "About" uri in the barcode web application.
      
      def get(): renders the about.html file located in templates.
"""
from flask import request, render_template
from flask.views import MethodView

class About(MethodView):
    def get(self):
        return render_template("about.html")