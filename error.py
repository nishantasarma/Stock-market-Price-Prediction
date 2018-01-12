import model as mdl
import numpy as np 
import matplotlib.pyplot as plt 


def error():

	results, test = mdl.model()
	errors = []

	for id, result in enumerate(results):

		error = abs(result-test[id])

		errors.append(error)


	errors = np.array(errors)

	mean_error = np.mean(errors)

	return mean_error