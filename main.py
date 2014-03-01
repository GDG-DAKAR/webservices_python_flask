# -*- coding: utf-8 -*- 

from flask import Flask, render_template, flash, session, redirect, request
from flask.ext.restful import Resource, Api, reqparse
from functions import *
from forms import * 



#Parsing args
parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('note', type=str)


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT-O_o'
api = Api(app)



#Note resource
class Note(Resource):
	""" docstring """
	def get(self,id=None):
		if id:
			return readNote(id)
		else:
			return getNotes()

	def post(self):
		args = parser.parse_args()
		return createNote(args['note'])

	def put(self,id):
		args = parser.parse_args()
		return updateNote(id, args['note'])

	def delete(self,id):
		return deleteNote(id)




api.add_resource(Note, '/', '/<int:id>')


@app.route('/web',methods=['GET', 'POST'])
def index():
	form = noteForm(request.form)

	#Post request
	if request.method == 'POST' and form.validate():
		note = form.note.data

		if createNote(note) != False:
				flash(u"Nouvelle note créée")
				return redirect('/web')
		else:
			return render_template('index.html', form=form, todos=todos)

	#Get request
	else:
		return render_template('index.html', form=form, notes=getNotes())

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)