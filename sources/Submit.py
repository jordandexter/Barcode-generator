"""
Name: Jordan Dexter
Date: March 6, 2024
Desc: This file defines the methods for the "Submit" uri in the barcode web application.
      
      def get(): renders the submit.html file located in templates with the selected image
      
      def post(): creates an instance of the model defined in model/Model.py and initiates the insertion process again (if the
                  user chooses to do so).     
"""

from flask import request, render_template, url_for, redirect
from flask.views import MethodView
from model.Model import model
import os

class Submit(MethodView):
    def get(self):
        curr_model = model()
        val = request.args['val']
        curr_model.select(val)

        return render_template('submit.html')

    def post(self):
        curr_model = model()
        val = request.form['submission']
        curr_model.insert(val)

        return redirect(url_for('submit', val=val))