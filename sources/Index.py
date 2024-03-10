"""
Name: Jordan Dexter
Date: March 6, 2024
Desc: This file defines the methods for the "Index" uri in the barcode web application.
      
      def get(): renders the index.html file located in templates.
      
      def post(): creates an instance of the model defined in model/Model.py and initiates the insertion process.     
"""
from flask import render_template, request, redirect, url_for
from flask.views import MethodView
from model.Model import model

class Index(MethodView):
    def get(self):
        return render_template('index.html')
    
    def post(self):
        curr_model = model()
        val = request.form['submission']
        curr_model.insert(val)
        return redirect(url_for('submit', val=val))