import pandas as pd

df = pd.read_csv("/content/spam.csv")
df.head()

df.groupby('Category').describe()

df['spam']=df['Category'].apply(lambda x: 1 if x=='spam' else 0)
df.head()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.Message,df.spam)

from sklearn.feature_extraction.text import CountVectorizer
v = CountVectorizer()
X_train_count = v.fit_transform(X_train.values)
X_train_count.toarray()[:2]

from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()
model.fit(X_train_count,y_train)

X_test_count = v.transform(X_test)
model.score(X_test_count, y_test)

from sklearn.pipeline import Pipeline
clf = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

clf.fit(X_train, y_train)

clf.score(X_test,y_test)

import pickle

model_filename = 'model.pkl'
with open(model_filename, 'wb') as model_file:
    pickle.dump(clf, model_file)
