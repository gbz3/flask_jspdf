from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return "hello world..."

@app.route('/pdf')
def pdf():
  return render_template('pdf.html')

