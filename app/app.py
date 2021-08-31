from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Flaskをインスタンス化
app = Flask(__name__)

##ここにDB定義


#エラーハンドリング
@app.errorhandler(404)
def not_found(error):
  return '404エラー'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload')
def upload():
  return render_template('upload.html')

@app.route('/upload_register', methods=['POST'])
def upload_register():
  title = request.form['title']
  if title:
    file = request.files['file']
    file_path = secure_filename(file.filename)
    file_path = 'static/' + file_path
    file.save(file_path)
    return file_path

if __name__ == "__main__":
    app.run(debug=True)
