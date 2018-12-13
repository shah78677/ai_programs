"""
CVR College of Engineering and Technology
Mtech Artificial Intelligence Lab Experiment
***Prediction of infant birth weight using Correlation and Linear Regression***
Written by Mir Habeebullah Shah Quadri (Mtech 1st year Dept. of AI)
Roll.No: 18B81DA914
Professor and Supervisor: Dr.Ponnusamy
"""

from scipy import stats
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style

x = [22, 25, 26, 28, 30, 31, 34, 36]
y = [3.5, 3.4, 3.3, 3.2, 3.1, 3, 2.9, 2.7]


def findCorr(x,y):
    p = stats.pearsonr(x,y)
    print("The correlation coefficient is: ", p[0])
    if p[0] < 0:
        print("Birth weight of an infant and mother's age are inversely related")
    elif p[0] == 0:
        print('There is no correlation')
    else:
        print("Birth weight of an infant and mother's age are positively related")

def slope(x_val, y_val):
    x = np.array(x_val)
    y = np.array(y_val)
    
    m = ( ( (np.mean(x) * np.mean(y)) - np.mean(x*y) ) /
          ((np.mean(x) * np.mean(x)) - np.mean(x*x)))
    m = round(m,2)
    b = (np.mean(y) - np.mean(x) * m)
    b = round(b, 2)

    return m, b

def regress(m, b, x):
    reg_line = [(m*i) + b for i in x]
    plt.scatter(x,y, color="red")
    plt.plot(x, reg_line)
    plt.ylabel('Birth Weight')
    plt.xlabel("Mother's age")
    plt.show()

findCorr(x, y)
m, b = slope(x, y)
regress(m, b, x)

print("Based on the regression analysis done on the dataset")
print("The weight of the infant should be in healthy range if the mother's age is between 23 to 30")
print("The weight of the infant should be on the lower range, if the mother's age is above 0 or below 23")
ip = input("To test this prediction, please provide an age for the mother: ")
x1 = int(ip)
f = m * x1 + b
print("If age of the mother is: ", x1, ", then the weight of the infant should be close to: ", f)
