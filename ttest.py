import numpy as np
from scipy import stats

x = [15.2, 15.3, 16.0, 15.8, 15.6, 14.9, 15.0, 15.4, 15.6, 15.7, 15.5, 15.2, 15.5, 15.1, 15.3, 15.0]
y = [15.9, 15.9, 15.2, 16.6, 15.2, 15.8, 15.8, 16.2, 15.6, 15.6, 15.8, 15.5, 15.5, 15.5, 14.9, 15.9]

mx =  np.mean(x)
my = np.mean(y)

stdx = np.std(x)
stdy = np.std(y)

varx = stdx ** 2
vary = stdy ** 2

n = 16

t_value = abs(mx - my) /  np.sqrt((varx / n) + (vary / n))
df = n + n - 2
p = 1 - stats.t.cdf(t_value, df)
print(p)
p = p*2
print("The T-Value is: ", t_value)
print("The P-Value is: ", p)
if t_value > p:
    print('We reject the null hypothesis')
else:
    print('We accept the null hypothesis')
