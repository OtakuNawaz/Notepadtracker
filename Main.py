from flask import Flask, render_template, flash,redirect,request,url_for
from flask_wtf import FlaskForm
from wtforms import Field,SubmitField,StringField,IntegerField,FloatField,TextAreaField
from wtforms.validators import DataRequired
from datetime import datetime
import os
import random

app=Flask(__name__)
app.config['SECRET_KEY']="my_super_secret_key"

class noteform(FlaskForm):
    folder_name=StringField('Name of the Folder')
    note_name=StringField('Name of the Note',validators=[DataRequired()])
    note_description=TextAreaField('Enter the details',validators=[DataRequired()])
    submit=SubmitField('Submit')
def git_functions():
    os.system('git checkout -b main')
    os.system('git add .')
    os.system('git commit -m "Added/Updated files - ID:{}{}"'.format(random.randint(10,99),random.randint(10,99)))
    os.system('git push -u origin main')
    print('Pushed Successfully')

@app.route('/',methods=['GET','POST'])
def first_page():
    return render_template('first_page.html')

@app.route('/addnote',methods=['GET','POST'])
def add_new_note():
    form=noteform()
    note_name=None
    note_description=None
    folder_name=None
    if form.validate_on_submit():
        note_name=form.note_name.data
        note_description=form.note_description.data
        folder_name=form.folder_name.data
        form.note_name.data=''
        form.note_description.data=''
        form.folder_name.data=''

        with open(f'{folder_name}\{note_name}.txt','w+') as f:
            f.write(f'{note_description}')
        flash('New Note Created Successfully')
        git_functions() 

    return render_template('add_note.html',form=form,note_name=note_name,note_description=note_description,folder_name=folder_name)

# @app.route('/editfilesfolder')
# def editfilesfolder():
#     form=noteform()
#     folder_name=None
#     if form.validate_on_submit():
#         folder_name=form.folder_name.data
#         form.folder_name.data=''
#     return render_template('Edit_files_folder.html',form=form,folder_name=folder_name)
if __name__=="__main__":
    app.run(debug=True)