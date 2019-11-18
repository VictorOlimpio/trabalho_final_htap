import pandas as pd
import mongodb_loader
from sklearn import preprocessing


data = mongodb_loader.read_mongo('car', 'cars')
# create the Labelencoder object
le = preprocessing.LabelEncoder()
columns = []
#convert the categorical columns into numeric
encoded_value = le.fit_transform(columns)



