import tensorflow as tf
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

print(tf.__version__)

df = pd.read_csv('arrhythmia.data', header=None)
data = df[[0,1,2,3,4,5]]
data.columns = ['age','sex','height','weight','QRS Duration', 'P-R Interval']

plt.rcParams['figure.figsize']
data.hist()

scatter_matrix(data)

###

df = pd.read_csv('auto-mpg.data', header=None, delim_whitespace=True)
print("df.head()", df.head())

plt.show()

