from scipy import stats

x = [22, 25, 26, 28, 30, 31, 34, 36]
y = [3.5, 3.4, 3.3, 3.2, 3.1, 3, 2.9, 2.7]

def findCorr(x,y):
    p = stats.pearsonr(x,y)
    print('Given data sets are: ')
    print('X: ', x)
    print('Y: ', y)
    print('The correlation coefficient of the given data sets is: ', p[0])
    if p[0] < 0:
        print('The data sets are inversely correlated')
    elif p[0] > 0:
        print('The data sets are positively correlated')
    else:
        print('There is no correlation between the given data sets')

findCorr(x,y)
