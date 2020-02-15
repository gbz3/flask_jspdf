from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return "hello world..."

@app.route('/jspdf')
def jspdf():
  return render_template('jspdf.html')

@app.route('/pdflib')
def pdflib():
  return render_template('pdf-lib.html')

