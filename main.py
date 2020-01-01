import pandas as pd
import numpy as np
import datetime
from sklearn.linear_model import LinearRegression

#Read the dataset, set the index as the Date column,
#converts the index’s type from “object” to “datetime64[ns]”
df = pd.read_csv('Google.csv', usecols=['Date', 'Close'], index_col=[0], 
                 date_parser=lambda x: datetime.datetime.strptime(x, "%Y-%m-%d"))

##check if there is any missing values
#df.isnull().values.any()

##check the distribution of the prices
#df.hist()

fit_params ={}

def best_fit(w, det_coef):
    def lin_reg(y):
        """Receive a sequence of values, ndarray, and apply a linear regression,
        based on a x axis of equaly espaced numbers.
        Return: the predicted value for the next number if the determination coef
        is above the det_coef or zero otherwise.
        """
    #   set the x axis based on the lenght of the ndarray
        x = np.array(list(range(len(y)))).reshape(-1,1)
    #   fit a linear regression
        lin = LinearRegression().fit(x, y)
    #   verify if r^2 is above the a certain value
        if lin.score(x,y) < det_coef:
            return 0
        else:
            return lin.predict([[w]])
    
    #create the column with the predicted values for each date
    df['Predicted'] = df.Close.rolling(w).apply(lin_reg, 'raw=True').shift(1)
    
    #create a bool column specifying if the values predicted are valid
    #df['valid'] = df.Predicted > 0
    
    #create a column with the diference of price expected for the next day
    df['Expected_diff']= df.Predicted - df.Close.shift()
    
    #create a column with the actual price difference
    df['Actual_diff']= df.Close.diff()
    
    #create a bool column to verify if the expected variation was positive
    df['Expected_pos'] = df.Expected_diff > 0
    
    #create a bool column to verify if the actual variation was positive
    df['Actual_pos'] = df.Actual_diff > 0
    
    #create a Profit column verifying if the sign of the prection was realized
    df['Profit'] = df.Expected_pos == df.Actual_pos
    
    
    #count the true profits on the rows where the predicted values are above zero
    win = sum(df[df.Predicted > 0].Profit)
    
    #count the total number of valid rows
    total = len(df[df.Predicted > 0])
    
    #calculate the ration between the wins and the total
    ratio = (win/total)
    
    return ratio


def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]
 
    
########################################################################
#Define parameters and run the model

# Variable that define the max size of the window to run the model
max_window = 30

# Variable that define the max r^2 to run the model, between 0 and 1
max_det_coef = 0.9

#loop to create a dictionary with the results for each parameter
for i in range(3,max_window):
#    R² defined between 0.3 and max_det_coef with 0.2 step
    for c in np.arange(0.3, max_det_coef, 0.2):
        ratio = best_fit(i, c)
        fit_params[(i, c)] = ratio

#get the dict key of best fit. It is a tuple (window, det_coef)
best_fit = keywithmaxval(fit_params)
#############################################################

print('The best won ratio was: ' + str(round(fit_params[best_fit]*100, 2)) +'%')
print('Window:', best_fit[0])
print('det_coef:', best_fit[1])

 
