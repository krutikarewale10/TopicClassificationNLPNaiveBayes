#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Libraries
import pandas as pd
import re
import string
# importing required libraries
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


# In[2]:


from sklearn.model_selection import train_test_split

# read the train and test dataset
data_train = pd.read_excel(open("C:/Python/Python3.8.2/KRU_PRACTISE/PYTHON/NLP/Text_Mining/training_data.xlsx",'rb'))
data_test = pd.read_excel(open("C:/Python/Python3.8.2/KRU_PRACTISE/PYTHON/NLP/Text_Mining/test_data.xlsx",'rb'))

data_train['Label'] = data_train['Type'].apply(lambda x: 0 if x=='Disease' else 1)
print(data_train)


# In[3]:


# shape of the dataset
print('Shape of training data :',data_train.shape)
print('Shape of testing data :',data_test.shape)


# In[4]:


'''
# Remove punctuation
data_train['Text'] = data_train['Text'].map(lambda data_train: re.sub(r'[^\w\s]', '', data_train))
data_train['Text'] = data_train['Text'].map(lambda x: x.lower())
data_train['Text'] = data_train['Text'].map(lambda x: x.split(' '))

# Remove punctuation
data_test['Text'] = data_test['Text'].map(lambda data_test: re.sub(r'[^\w\s]', '', data_test))
data_test['Text'] = data_test['Text'].map(lambda x: x.lower())
data_test['Text'] = data_test['Text'].map(lambda x: x.split(' '))
'''


# In[5]:


# seperate the independent and target variable on training data
#train_x = data_train.drop(columns=['Type',],axis=1)
#train_y = data_train['Type']
#train_x = train_x[:1900]
#train_y = train_y[:1900]

from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test=train_test_split(train_x,train_y,random_state=101,test_size=0.3)
# seperate the independent and target variable on testing data
#test_x = data_test.drop(columns=['Type'],axis=1)
#test_y = data_test['Type']
#test_x = test_x[:1901]
#test_y = test_y[:1912]
X = data_train['Text']
Y = data_train['Label']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.01, shuffle=False)


# In[6]:


from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(strip_accents='ascii', token_pattern=u'(?ui)\\b\\w*[a-z]+\\w*\\b', lowercase=True, stop_words='english')
X_train_cv = cv.fit_transform(X_train)
X_test_cv = cv.transform(X_test)


# In[7]:


# Convert to bag of words


# In[ ]:





# In[8]:


from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train_cv, y_train)
predictions = naive_bayes.predict(X_test_cv)


# In[9]:


word_freq_df = pd.DataFrame(X_train_cv.toarray(), columns=cv.get_feature_names())
top_words_df = pd.DataFrame(word_freq_df.sum()).sort_values(0, ascending=False)


# In[10]:


from sklearn.metrics import accuracy_score, precision_score, recall_score
print('Accuracy score: ', accuracy_score(y_test, predictions))
print('Precision score:', precision_score(y_test, predictions))
print('Recall score:', recall_score(y_test, predictions))


# In[11]:


from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
cm = confusion_matrix(y_test, predictions)
sns.heatmap(cm, square=True, annot=True, cmap='RdBu', cbar=False,
xticklabels=['Disease', 'Weather'], yticklabels=['Disease', 'Weather'])
plt.xlabel('true label')
plt.ylabel('predicted label')


# In[12]:


testing_predictions = []
for i in range(len(X_test)):
    if predictions[i] == 1:
        testing_predictions.append('Weather')
    else:
        testing_predictions.append('Disease')
check_df = pd.DataFrame({'actual_label': list(y_test),'prediction': testing_predictions, 'Text':list(X_test)})
check_df.replace(to_replace=0, value='Disease', inplace=True)
check_df.replace(to_replace=1, value='Weather', inplace=True)
print(check_df)


# In[49]:


print(testing_predictions)


# In[ ]:





# In[ ]:





# In[ ]:




