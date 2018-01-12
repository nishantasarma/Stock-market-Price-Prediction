import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

def preprocess():
	df_x = pd.read_csv('/home/bee/Desktop/minor project/aapl .csv', usecols=['Date','Close','Volume'])
	df_x.Date = pd.to_datetime(df_x.Date)
	df_x = df_x.set_index('Date')
	df_x = df_x.sort_index(ascending='True')
	df_x = df_x.resample('D')
	df_x = df_x.interpolate('linear')
	df = df_x.loc['2017-08-31']
	df_y = df_x.loc['2017-08-02':'2017-08-30']
	df_x = df_x.loc['2017-08-01':'2017-08-30']
	df_x1 = pd.read_csv('/home/bee/Desktop/minor project/views.csv')
	views = np.asarray(df_x1)
	df_x['Googles_result'] = views
	df_y = df_y.append(df)
	df_x.Close = df_x.Close.apply(np.float64)
	df_x.Volume = df_x.Volume.apply(np.float64)
	df_x.Googles_result = df_x.Googles_result.apply(np.float64)
	df_y = df_y.Close
	return df_x, df_y