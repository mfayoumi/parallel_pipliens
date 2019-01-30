import numpy as np 
import pandas as pd
import re
import config 
import feature_extraction
from sklearn.pipeline import FeatureUnion
from sklearn.pipeline import Pipeline

## Reading your CSV file using pandas
file_name = config.full_file_path
df = pd.read_csv(file_name)

feats = FeatureUnion([
                      ('column1', feature_extraction.column1),
                      ('column2', feature_extraction.column2),
                      ('column3', feature_extraction.column3),
                      ('column4', feature_extraction.column4),
                    ])

feature_processing = Pipeline([('feats', feats)])
## @@ Now you can fit your ML Model after preparing the training set and testing set
#feature_processing.fit_transform(X_train)