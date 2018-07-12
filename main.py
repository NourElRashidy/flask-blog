from flask import Flask, jsonify, request, redirect, render_template
from db import db

app = Flask(__name__)
# app.debug = True

@app.route('/')
def list_posts():
    posts = db.get_posts()
    resp = []
    for post in posts:
        resp.append({'title':post.title, 'id':post.id})
    # print('posts')
    return jsonify(resp)

@app.route('/create', methods = ['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        db.add_post(request.form['author'], request.form['title'], request.form['body'])
        return redirect('/')
    else:
        return render_template('create_post.html')

app.run(host='127.0.0.1', port=5000, debug=False)
