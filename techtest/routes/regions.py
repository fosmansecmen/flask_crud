from flask import abort, jsonify, request, render_template, redirect, url_for

import json
from techtest.baseapp import app
from techtest.connector import db_session_wrap, db_session
from techtest.models.region import Region


# @app.route('/regions', methods=['GET'])
@db_session_wrap
def get_regions(session):
    query = session.query(
        Region
    ).order_by(
        Region.id
    )
    return json.dumps([region.asdict() for region in query.all()])


# create
@app.route('/regions/insert', methods = ['POST'])
def insert_regions():
    values = request.form.to_dict(flat=False)
    if request.method == 'POST':
        code = values['code'][0]
        name = values['name'][0]

        region = Region(code=code, name=name)

        with db_session() as session:
            session.add(region)

        return redirect(url_for('index_regions'))


# read
@app.route('/regions/', methods=['GET'])
def index_regions():
    all_data = json.loads(get_regions())
    print(all_data)
 
    return render_template("regions.html", regions = all_data)



# update
@app.route('/regions/update', methods = ['GET', 'POST'])
def update_regions():

    values = request.form.to_dict(flat=False)
    if request.method == 'POST':
        region_id = values['id'][0]

        # get the article to be updated
        region = Region.query.get(region_id)

        region.code = values['code'][0]
        region.name = values['name'][0]
        

        with db_session() as session:
            session.commit()

        return redirect(url_for('index_regions'))


# delete
@app.route('/regions/delete/<id>/', methods = ['GET', 'POST'])
def delete_regions(id):
    region = Region.query.get(id)
    
    with db_session() as session:
        session.delete(region)

    return redirect(url_for('index_regions'))
 