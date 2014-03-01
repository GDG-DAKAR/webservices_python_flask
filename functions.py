# -*- coding: utf-8 -*- 

from sqlalchemy.orm import sessionmaker
from db import *




# def checkout_listener(dbapi_con, con_record, con_proxy):
#     try:
#         try:
#             dbapi_con.ping(False)
#         except TypeError:
#             dbapi_con.ping()
#     except dbapi_con.OperationalError as exc:
#         if exc.args[0] in (2006, 2013, 2014, 2045, 2055):
#             raise DisconnectionError()
#         else:
#             raise

# verbose=False #Set to True to enable verbose
# engine = create_engine('sqlite:///database',
#                           pool_size=100,
#                           pool_recycle=3600,
#                           echo=verbose)
# event.listen(engine, 'checkout', checkout_listener)




verbose=False #Set to True to enable verbose
engine = create_engine('sqlite:///database', echo=verbose)



#This method initiate a db session
def getSession():
	Session = sessionmaker(bind=engine)
	return Session()




#Create a new note
def createNote(note):
	session=getSession()

	note = Note(note=note)

	try:
		session.add(note)
		session.commit()
		return note.id
	except:
		return False
	finally:
		session.close()


#Edit a note
def updateNote(note_id, new_note):
	session=getSession()

	try:
		q = session.query(Note).filter(Note.id==note_id).all()[0]
		q.note = new_note
		session.commit()
		return True
	except:
		return False
	finally:
		session.close()




#Retrieve all notes
def getNotes():
	session=getSession()
	notes=[]
	try:
		req = session.query(Note).all()
		for q in req:
			notes.append({'id':q.id, 'note':q.note, 'date':str(q.date)})
		return notes
	except:
		return False
	finally:
		session.close()


	

#Retrieve a specific note
def readNote(note_id):
	session=getSession()
	
	try:
		q = session.query(Note).filter(Note.id==note_id).all()[0]
		return {'id':q.id, 'note':q.note, 'date':str(q.date)}
	except:
		return False
	finally:
		session.close()


	

#Delete a specific note
def deleteNote(note_id):
	session=getSession()
	
	try:
		q = session.query(Note).filter(Note.id==note_id).all()[0]
		session.delete(q)
		session.commit()
		return True
	except:
		return False
	finally:
		session.close()



#Empty db
def emptyDB():
	session=getSession()
	try:
		q = session.query(Note).all()
		for note in q:
			session.delete(note)
		session.commit()
		return True
	except:
		return False
	finally:
		session.close()