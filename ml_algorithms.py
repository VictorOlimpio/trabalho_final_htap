from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.svm import LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from yellowbrick.classifier import ClassificationReport

class MLAlgorithms():
    gnb_model = GaussianNB()
    svc_model = LinearSVC(random_state=0)
    knn_model = KNeighborsClassifier(n_neighbors=3)

    def get_gnb_model(self):
        return self.gnb_model

    def get_svc_model(self):
        return self.svc_model

    def get_knn_model(self):
        return self.knn_model

    def naive_bayes(self, data_train, data_test, target_train, target_test):
        pred = self.gnb_model.fit(data_train, target_train).predict(data_test)
        print("Naive-Bayes accuracy : ", accuracy_score(target_test, pred, normalize=True))

    def svm(self, data_train, data_test, target_train, target_test):
        pred = self.svc_model.fit(data_train, target_train).predict(data_test)
        print("LinearSVC accuracy : ", accuracy_score(target_test, pred, normalize=True))

    def knn(self, data_train, data_test, target_train, target_test):
        pred = self.knn_model.fit(data_train, target_train).predict(data_test)
        print("KNeighbors accuracy score : ", accuracy_score(target_test, pred))

    def results(self, algorithm, data_train, data_test, target_train, target_test):
        visualizer = ClassificationReport(algorithm, classes=['1', '0'])
        visualizer.fit(data_train, target_train)
        visualizer.score(data_test, target_test)
        visualizer.show()