from componentes.chars import plot_confusion_matrix
import streamlit as st
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import GridSearchCV
import pandas as pd

def train_knn(X_train, y_train, X_test, y_test, n_neighbors=5):
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    st.write("### Resultados do KNN")
    st.write("Acurácia:", accuracy_score(y_test, y_pred))
    
    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    st.write("#### Relatório de Classificação")
    st.dataframe(report_df.style.format("{:.2f}"))
    
    plot_confusion_matrix(y_test, y_pred)

def train_svm(X_train, y_train, X_test, y_test, C=1.0, kernel="linear"):
    model = SVC(C=C, kernel=kernel)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    st.write("### Resultados do SVM")
    st.write("Acurácia:", accuracy_score(y_test, y_pred))
    
    report = classification_report(y_test, y_pred, output_dict=True)
    report_df = pd.DataFrame(report).transpose()
    st.write("#### Relatório de Classificação")
    st.dataframe(report_df.style.format("{:.2f}"))
    
    plot_confusion_matrix(y_test, y_pred)

def hyperparameter_tuning_knn(X, y):
    param_grid = {'n_neighbors': [1, 3, 5, 7, 9]}
    grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)
    grid_search.fit(X, y)
    
    st.write("### Melhores Hiperparâmetros para KNN:", grid_search.best_params_)
    st.write("Melhor Acurácia:", grid_search.best_score_)

def hyperparameter_tuning_svm(X, y):
    param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf', 'poly']}
    grid_search = GridSearchCV(SVC(), param_grid, cv=5)
    grid_search.fit(X, y)
    
    st.write("### Melhores Hiperparâmetros para SVM:", grid_search.best_params_)
    st.write("Melhor Acurácia:", grid_search.best_score_)
