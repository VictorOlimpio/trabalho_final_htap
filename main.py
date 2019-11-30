from time import sleep

import mongodb_loader
from sklearn import preprocessing
import seaborn as sns
import matplotlib.pyplot as plt

def time_wait():
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)

print('Connecting to databese.')
time_wait()
data = mongodb_loader.read_mongo('crimes_data', 'crimes')
print('Importing dataset:')
time_wait()
print('Displaying dataset imported:')
sleep(1)
print(data)

exited = False

while not exited:

    if not data.empty:
        sns.set(style="whitegrid", color_codes=True)
        print('Analizing dataset:')
        # setting the plot size for all plots
        sns.set(rc={'figure.figsize':(12,11)})
        time_wait()
        # create a countplot
        sns.countplot(y='OFFENSE_CATEGORY_ID',data=data, hue='OFFENSE_CATEGORY_ID')
        # Remove the top and down margin
        sns.despine(offset=10, trim=True)
        print('Showing data distribuition.')
        # display the plotplt.show()
        plt.show()
        # create the Labelencoder object
        le = preprocessing.LabelEncoder()
        columns = ['OFFENSE_CATEGORY_ID']
        #convert the categorical columns into numeric
        encoded_value = le.fit_transform(columns)

        print('To exit type "exit"')
        anwser = input()
        if anwser == 'exit':
            exited = True


