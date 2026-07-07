import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split 
class Algorithm():
    
    def split_scalar(indep_X,dep_Y):
            X_train, X_test, y_train, y_test = train_test_split(indep_X, dep_Y, test_size = 0.2, random_state = 0)
            sc = StandardScaler()
            X_train = sc.fit_transform(X_train)
            X_test = sc.transform(X_test)    
            return X_train, X_test, y_train, y_test
    
    def r2_prediction(regressor,X_test,y_test):
         y_pred = regressor.predict(X_test)
         from sklearn.metrics import r2_score
         r2=r2_score(y_test,y_pred)
         return r2
     
    def Linear(X_train,y_train,X_test,y_test):       
            # Fitting K-NN to the Training set
            from sklearn.linear_model import LinearRegression
            regressor = LinearRegression()
            regressor.fit(X_train, y_train)
            r2=Algorithm.r2_prediction(regressor,X_test,y_test)
            return  regressor,r2   
        
    def svm_linear(X_train,y_train,X_test,y_test):
                    
            from sklearn.svm import SVR
            regressor = SVR(kernel = 'linear')
            regressor.fit(X_train, y_train)
            r2=Algorithm.r2_prediction(regressor,X_test,y_test)
            return  regressor,r2 
        
    def Decision(X_train,y_train,X_test,y_test):
            
            # Fitting K-NN to the Training setC
            from sklearn.tree import DecisionTreeRegressor
            regressor = DecisionTreeRegressor(random_state = 0)
            regressor.fit(X_train, y_train)
            r2=Algorithm.r2_prediction(regressor,X_test,y_test)
            return  regressor,r2  
         
    
    def random(X_train,y_train,X_test,y_test):       
            # Fitting K-NN to the Training set
            from sklearn.ensemble import RandomForestRegressor
            regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)
            regressor.fit(X_train, y_train)
            r2=Algorithm.r2_prediction(regressor,X_test,y_test)
            return  regressor,r2 
        
    def regression(acclin,accsvml,accdes,accrf): 
        
        rfedataframe=pd.DataFrame(index=['R_Score'],columns=['Linear','SVMl','Decision','Random'])
     
        for number,idex in enumerate(rfedataframe.index):
    
            rfedataframe['Linear'][idex]=acclin[number]       
            rfedataframe['SVMl'][idex]=accsvml[number]
            rfedataframe['Decision'][idex]=accdes[number]
            rfedataframe['Random'][idex]=accrf[number]
        return rfedataframe