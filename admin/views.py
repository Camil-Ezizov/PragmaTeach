from app import app
from flask import render_template,redirect,request,url_for
@app.route('/admin')
def adminIndex():
    return render_template('/admin/index.html',title='Dashboard')