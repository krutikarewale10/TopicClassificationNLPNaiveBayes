#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request
from flask import make_response
from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
import numpy as np
import joblib


# In[2]:


loaded_model=joblib.load("C:/Python/Python3.8.2/KRU_PRACTISE/PYTHON/WEB_APPLICATION/pkl/model.pkl")
loaded_stop=joblib.load("C:/Python/Python3.8.2/KRU_PRACTISE/PYTHON/WEB_APPLICATION/pkl/stopwords.pkl")
loaded_vec=joblib.load("C:/Python/Python3.8.2/KRU_PRACTISE/PYTHON/WEB_APPLICATION/pkl/vectorizer.pkl")


# In[3]:


app = Flask(__name__)


# In[4]:


def classify(document):
 label = {0: 'Disease', 1: 'Weather'}
 X = loaded_vec.transform([document])
 y = loaded_model.predict(X)[0]
 proba = np.max(loaded_model.predict_proba(X))
 return y, proba


# In[5]:


class Textdata(Form):
 datatext = TextAreaField('',[validators.DataRequired(),validators.length(min=15)])
'''
class ReviewForm(Form):
 moviereview = TextAreaField(‘’,[validators.DataRequired(),validators.length(min=15)])
 '''

# In[6]:


@app.route('/')
def index():
 form = Textdata(request.form)
 return render_template('textdata.html', form=form)
print('HI')

'''
@app.route(‘/’)
def index():
 form = ReviewForm(request.form)
 return render_template(‘reviewform.html’, form=form)
'''
# In[ ]:

@app.route('/results', methods=['POST'])
def results():
 form = Textdata(request.form)
 if request.method == 'POST' and form.validate():
        Text = request.form['datatext']
        y, proba = classify(Text)
        return render_template('results.html',content=Text,prediction=y,probability=round(proba*100, 2))
        return render_template('textdata.html', form=form)

if __name__ == '__main__':
 app.run(debug=True, use_reloader=False)




'''
@app.route(‘/results’, methods=[‘POST’])
def results():
 form = ReviewForm(request.form)
 if request.method == ‘POST’ and form.validate():
 review = request.form[‘moviereview’]
 y, proba = classify(review)
 return render_template(‘results.html’,content=review,prediction=y,probability=round(proba*100, 2))
 return render_template(‘reviewform.html’, form=form)
if __name__ == ‘__main__’:
 app.run(debug=True)
'''


# In[ ]:





# In[ ]:





# In[ ]:




