from time import sleep

import mongodb_loader
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from ml_algorithms import MLAlgorithms
import ux

def db_import():
    print('Connecting to the database:')
    ux.time_wait()
    data = mongodb_loader.read_mongo('crimes_data', 'crimes')
    print('Importing dataset:')
    ux.time_wait()
    print('Displaying dataset imported:')
    print(data)
    sleep(1)
    return data

def encoding_values(data):
    le = preprocessing.LabelEncoder()
    data['OFFENSE_TYPE_ID'] = le.fit_transform(data['OFFENSE_TYPE_ID'])
    data['OFFENSE_CATEGORY_ID'] = le.fit_transform(data['OFFENSE_CATEGORY_ID'])
    data['NEIGHBORHOOD_ID'] = le.fit_transform(data['NEIGHBORHOOD_ID'])
    data['IS_CRIME'] = le.fit_transform(data['IS_CRIME'])
    data['IS_CRIME'] = le.fit_transform(data['IS_TRAFFIC'])
    return data

def plot_data(data, column='IS_CRIME'):
    sns.set(style="whitegrid", color_codes=True)
    print('Analizing dataset:')
    # setting the plot size for all plots
    sns.set(rc={'figure.figsize': (8, 6)})
    ux.time_wait()
    # create a countplot
    sns.countplot(y=column, data=data, hue=column)
    # Remove the top and down margin
    sns.despine(offset=10, trim=True)
    print('Showing data distribuition.')
    # display the plotplt.show()
    plt.show()


def main():

    exited = False
    data = db_import()

    while not exited:

        if not data.empty:
            print('Type 1 to show class distribution.')
            print('Tyep 2 to generate test and training sets, and choice an algorithm')
            choice = input()
            if choice == '1': plot_data(data)
            if choice == '2':
                print('Converting categorical data.')
                ux.time_wait()
                # convert the categorical columns into numeric
                data = encoding_values(data)
                columns = ['OFFENSE_TYPE_ID', 'OFFENSE_CATEGORY_ID', 'NEIGHBORHOOD_ID']
                selected_columns = [col for col in data.columns if col in columns]

                data_selected = data[selected_columns]
                target_data = data['IS_CRIME']

                print('Generating test and training sets.')
                ux.time_wait()

                data_train, data_test, target_train, target_test = train_test_split(data_selected, target_data,
                                                                                    test_size=0.10,
                                                                                    random_state=10)

                print('Type knn to run the KNN classifier.')
                print('Type nb to run the Naive Bayes classifier.')
                print('Type svm to run the LinearSVC classifier.')
                choice = input()
                options = ['knn', 'nb', 'svm']
                if choice in options:
                    ml_algorithms = MLAlgorithms()
                    if choice == 'knn':
                        print('Running KNN.')
                        ml_algorithms.results(ml_algorithms.get_knn_model(), data_train, data_test, target_train,
                                              target_test)
                    elif choice == 'nb':
                        print('Running Naive Bayes.')
                        ml_algorithms.results(ml_algorithms.get_gnb_model(), data_train, data_test, target_train,
                                              target_test)
                    else:
                        print('Running LinearSVC.')
                        ml_algorithms.results(ml_algorithms.get_svc_model(), data_train, data_test, target_train,
                                              target_test)
            if choice != '1' and choice != '2': exited = ux.exit_input()


if __name__== "__main__":
  main()
