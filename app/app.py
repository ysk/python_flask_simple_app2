from flask import Flask, render_template, request, redirect, url_for, flash
from flask.helpers import url_for
from werkzeug.utils import redirect, secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from upload_cloud import upload_cloud
from paste_cloud import paste_cloud

# Flaskをインスタンス化
app = Flask(__name__)

##ここにDB定義
URI = 'sqlite:///sample.db'
app.config['SQLALCHEMY_DATABASE_URI'] = URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class DB(db.Model):
  __tablename__ = 'test_table'
  id        = db.Column(db.Integer, primary_key=True)
  title     = db.Column(db.String(30), unique=True)
  file_path = db.Column(db.String(64))
  data      = db.Column(db.DateTime, nullable=False, default=datetime.today())


@app.cli.command('initialize_DB')
def initialize_DB():
  db.create_all()

#エラーハンドリング
@app.errorhandler(404)
def not_found(error):
  return '404エラー'


@app.route('/')
def index():
  registration_data = DB.query.all()
  return render_template('index.html', registration_data=registration_data)


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
    
    # upload_cloud関数を実装する
    result_path = upload_cloud(file_path)
    register_file = DB(title=title, file_path=result_path)
    db.session.add(register_file)
    db.session.commit(register_file)
    flash('結果ファイルが用意できました')
    return redirect(url_for('index'))
  else:
    flash('タイトルを入力してもう一度やり直してください')
    return redirect(url_for('index'))


@app.route('/paste')
def paste():
  title = request.form['title']
  if title:
    paste_data = request.files['paste_data']

    # paste_cloud関数を実装する
    result_path = paste_cloud(title, paste_data)
    register_file = DB(title=title, file_path=result_path)
    db.session.add(register_file)
    db.session.commit(register_file)
    flash('結果ファイルが用意できました')
    return redirect(url_for('index'))
  else:
    flash('タイトルを入力してもう一度やり直してください')
    return redirect(url_for('index'))


@app.route('/paste_register', methods=['POST'])
def paste_register():
  title = request.form['title']
  if title:
    paste_data = request.form['paste_data']
    return paste_data


if __name__ == "__main__":
    app.run(debug=True)

