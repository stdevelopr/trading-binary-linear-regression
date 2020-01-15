# TradingBinary-LinearRegression
Algorithm to predict the best parameters in a linear regression to trade binary options.


## Challenge:
To predict if the next closing price will be higher or lower, based on a linear regression model.


### Method
Using the linear regression model, assume that the next closing price will be the value predicted by the model.
* If the actual value is above the predicted, the guess is that the next closing price will get lower.
* If the actual value is below the predicted, the guess is that the next closing price will get higher.

#### Parameters
The following parameters will be under control:
* The size of the window in wich the regression line will be calculated. 
* The dispersion around the line, through the coeficient of determination
varying from 0 ( total dispersion) to 1 (concentrated on the line)

___
## Results

Running the algorithm with a window size varying from 3 to 30 and the coeficient of determination varying from 0.3 to 0.9 
with 0.2 step, the best result was:

- Win ratio: 54.92%
- Window size: 27
- Coefficient of determination: 0.9

___
## Prediction Plot
Here we see all the closing prices as the small blue dots. The red ones are the points that fitted the rule of the coefficient of determination. The green stars are ones where it was possible to make profit.
![alt tag](/image_plot/BestPredicted.png)

In the zoom we can see that the predictions and profits are mostly concentrated where the dispersion is small and the prices follow almost linearly.
![alt tag](/image_plot/BestPredicted_Zoom.png)
## Conclusion

After running trough the whole dataset 108 times with 108 different parameters:\
The avarage win ratio was 0.49\
Standard deviation: 0.016

So, running this strategy in one dataset without caring about the parameters will probably result in loss most of the time.
After adjusting the parameters it was possible to find a combination that resulted in a positive win ratio of 4.9%.
It was noted that the entry points were few, however.
