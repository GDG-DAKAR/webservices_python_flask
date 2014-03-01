# -*- coding: utf-8 -*-
from wtforms import *
  
  
class noteForm(Form):
	""" Note Form  """
	note = TextField(u'Note', [validators.length(min=5), validators.required()])