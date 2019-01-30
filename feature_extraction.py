from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler
from binary_Estimator import TextSelector, NumberSelector

## Preparing the parrallel piplines

column1 = Pipeline([
                ('selector', TextSelector(key='column1')),
                ('CountVectorizer', CountVectorizer( stop_words='english'))
            ])
column2 = Pipeline([
                ('selector', TextSelector(key='column2')),
                ('CountVectorizer', CountVectorizer( stop_words='english'))
            ])
column3 = Pipeline([
                ('selector', TextSelector(key='column3')),
                ('CountVectorizer', CountVectorizer( stop_words='english'))
            ])

# Assume column4 is numeric column
column4 = Pipeline([
                ('selector', NumberSelector(key='column4')),
                ('CountVectorizer', CountVectorizer( stop_words='english'))
            ])

# You can use both CountVectorizer object or TfidfVectorizer
'''

column1 = Pipeline([
                ('selector', TextSelector(key='column1')),
                ('tfidf', TfidfVectorizer( stop_words='english'))
            ])
column2 = Pipeline([
                ('selector', TextSelector(key='column2')),
                ('tfidf', TfidfVectorizer( stop_words='english'))
            ])
column3 = Pipeline([
                ('selector', TextSelector(key='column3')),
                ('tfidf', TfidfVectorizer( stop_words='english'))
            ])
column4 = Pipeline([
                ('selector', TextSelector(key='column4')),
                ('tfidf', TfidfVectorizer( stop_words='english'))
            ])
'''

