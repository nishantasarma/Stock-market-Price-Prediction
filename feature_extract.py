import numpy as np 
import pandas as pd 
import preprocess as p 


def feature_extract():
	df_x, df_y = p.preprocess()
	df_x['mov_avg_close'] = df_x.Close.rolling(window=2).mean()
	where_are_NaNs = np.isnan(df_x.mov_avg_close)
	df_x.mov_avg_close[where_are_NaNs] = 0
	df_x['momentum'] = 0
	df_x['momentum'] = rate_of_change(df_x.momentum,df_x.Close)
	#df_x['roc_volume'] = 0
	#df_x['roc_volume'] = rate_of_change(df_x.roc_volume,df_x.Volume)
	return df_x, df_y


def rate_of_change(values, column):

	for id, value in enumerate(column):
		if id >= 1:
			values[id] =(column[id] - column[id-1])*100

	return values		
