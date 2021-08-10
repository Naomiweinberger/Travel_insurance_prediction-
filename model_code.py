def run_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)

    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)    
    cnf_matrix_test = confusion_matrix(y_test,  y_pred_test)

    print('Confusion Matrix for Test Set:\n', cnf_matrix_test)
   
    cnf_matrix_train = confusion_matrix(y_train,  y_pred_train)
    print('Confusion Matrix for Train Set:\n', cnf_matrix_train)
 
    print('Classification Report for Test Set:\n',classification_report(y_test , y_pred_test))
    print('Classification Report for Train Set:\n',classification_report(y_train, y_pred_train))
    return model 