from time import sleep

def time_wait():
    print('.')
    sleep(1)
    print('.')
    sleep(1)
    print('.')
    sleep(1)

def exit_input():
    print('To leave the program type "exit" or ENTER to continue.')
    anwser = input()
    if anwser == 'exit':
       return True
    return False

def input_choices():
    print('Type 1 to show class distribution.')
    print('Tyep 2 to choice an algorithm')
    choice = input()
    if choice == 2:
        print('Type knn to run the KNN classifier.')
        print('Type nb to run the Naive Bayes classifier.')
        print('Type svm to run the LinearSVC classifier.')
        choice = input()
        options = ['knn', 'nb', 'svm']
        if choice in options:
            return choice
    return choice