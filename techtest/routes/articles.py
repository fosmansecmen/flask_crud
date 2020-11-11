from flask import abort, jsonify, request, render_template, redirect, url_for

import json
from techtest.baseapp import app
from techtest.connector import db_session_wrap, db_session
from techtest.models.article import Article
from techtest.models.region import Region
from techtest.models.author import Author

from techtest.routes.authors import get_authors
from techtest.routes.regions import get_regions

@db_session_wrap
def get_articles(session):
    query = session.query(
        Article
    ).order_by(
        Article.id
    )
    return json.dumps([
        article.asdict(follow=['regions', 'authors']) for article in query.all()
    ])


# create
@app.route('/articles/insert', methods = ['POST'])
def insert_articles():
	values = request.form.to_dict(flat=False)
	if request.method == 'POST':
		title = values['title'][0]
		content = values['content'][0]
		
		regions = [Region.query.get(region)  for region in values['regions'] ]
		# print('***********regions:', regions)

		authors = [Author.query.get(author)  for author in values['authors'] ]
		# print('***********authors:', authors)

		article = Article(title=title, content=content, regions=regions, authors=authors)

		with db_session() as session:
			session.add(article)

		return redirect(url_for('index_articles'))


# read
@app.route('/articles/', methods=['GET'])
def index_articles():
    articles = json.loads(get_articles())
    regions = json.loads(get_regions())
    authors = json.loads(get_authors())
    # print('articles:', articles)
    # print('regions:', regions)
    # print('authors:', authors)
 
    return render_template("articles.html", articles = articles, regions = regions, authors= authors)
 

# update
@app.route('/articles/update', methods = ['GET', 'POST'])
def update_articles():

	values = request.form.to_dict(flat=False)
	if request.method == 'POST':
		article_id = values['id'][0]

		# get the article to be updated
		article = Article.query.get(article_id)

		article.title = values['title'][0]
		article.content = values['content'][0]
		
		article.regions = [Region.query.get(region)  for region in values['regions'] ]
		# print('***********regions:', regions)

		article.authors = [Author.query.get(author)  for author in values['authors'] ]
		# print('***********authors:', authors)

		with db_session() as session:
			session.commit()

		return redirect(url_for('index_articles'))


# delete
@app.route('/articles/delete/<id>/', methods = ['GET', 'POST'])
def delete_articles(id):
    article = Article.query.get(id)
    
    with db_session() as session:
    	session.delete(article)

    return redirect(url_for('index_articles'))