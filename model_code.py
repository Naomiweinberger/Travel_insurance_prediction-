def run_model(model, X_train, X_test, y_train, y_test):
    import pandas as pd
    import numpy as np
    import matplotlib as plt 
    import  csv
    from sklearn.preprocessing import StandardScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.pipeline import Pipeline
    from model_code import run_model
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import cross_val_score
    print('Training R^2 :', model.score(X_train, y_train))
    y_pred_train = model.predict(X_train)
    print('Training Root Mean Square Error', np.sqrt(metrics.mean_squared_error(y_train, y_pred_train)))
    print('\n----------------\n')
    print('Testing R^2 :', model.score(X_test, y_test))
    y_pred_test = model.predict(X_test)
    print('Testing Root Mean Square Error', np.sqrt(metrics.mean_squared_error(y_test, y_pred_test)))
    cnf_matrix = confusion_matrix(y_test, y_hat_test)
    print('Confusion Matrix:\n', cnf_matrix)
    plot_confusion_matrix(logreg, X_test, y_test,
                     cmap=plt.cm.Blues)
    plt.show()
    print(classification_report(y_true, y_pred, target_names=target_names))

