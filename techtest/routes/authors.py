from flask import abort, jsonify, request, render_template, redirect, url_for

import json
from techtest.baseapp import app
from techtest.connector import db_session_wrap, db_session
from techtest.models.author import Author


# @app.route('/authors', methods=['GET'])
@db_session_wrap
def get_authors(session):
    query = session.query(
        Author
    ).order_by(
        Author.id
    )
    return json.dumps([author.asdict() for author in query.all()])



# create
@app.route('/authors/insert', methods = ['POST'])
def insert_authors():
    values = request.form.to_dict(flat=False)
    if request.method == 'POST':
        first_name = values['first_name'][0]
        last_name = values['last_name'][0]

        author = Author(first_name=first_name, last_name=last_name)

        with db_session() as session:
            session.add(author)

        return redirect(url_for('index_authors'))


# read
@app.route('/authors/', methods=['GET'])
def index_authors():
    all_data = json.loads(get_authors())
    print(all_data)
 
    return render_template("authors.html", authors = all_data)



# update
@app.route('/authors/update', methods = ['GET', 'POST'])
def update_authors():

    values = request.form.to_dict(flat=False)
    if request.method == 'POST':
        author_id = values['id'][0]

        # get the article to be updated
        author = Author.query.get(author_id)

        author.first_name = values['first_name'][0]
        author.last_name = values['last_name'][0]
        

        with db_session() as session:
            session.commit()

        return redirect(url_for('index_authors'))


# delete
@app.route('/authors/delete/<id>/', methods = ['GET', 'POST'])
def delete_authors(id):
    author = Author.query.get(id)
    
    with db_session() as session:
        session.delete(author)

    return redirect(url_for('index_authors'))
 