import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import feature_extract as f
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import preprocessing

def model():

	df_x, df_y = f.feature_extract()
	dates = df_y.index
	y_set = np.asarray(df_y)
	x_set = np.asarray(df_x)
	X_train, X_test, y_train, y_test = train_test_split(x_set, y_set, test_size=0.2,random_state=0)

	scalar_x = preprocessing.StandardScaler().fit(X_train)
	X_scaled = scalar_x.transform(X_train)
	X_test_scaled = scalar_x.transform(X_test)

	clf = svm.SVR(kernel='rbf', C=1e3, gamma=0.1).fit(X_scaled, y_train)
	mdl_plot = clf.predict(X_scaled) 
	result = clf.predict(X_test_scaled)

	plt.xlabel('dates')
	plt.ylabel('prices')
	plt.scatter(dates[0:24], mdl_plot)
	plt.plot(dates[0:24], mdl_plot)
	plt.grid()
	plt.legend()
	plt.show()
	return result, y_test