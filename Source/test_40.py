'''
	test_40.py

	"Top Israeli prof claims simple stats show 
	virus plays itself out after 70 days. [regardless of measures taken]".
	These countries did not take measures: Singapore, Taiwan, and Sweden.
	https://www.timesofisrael.com/top-israeli-prof-claims-simple-stats-show-virus-plays-itself-out-after-70-days/

	This code is used to validate this statement.

	Uses CSV Data from:
	https://github.com/owid/covid-19-data/tree/master/public/data

	April 2020
'''
import argparse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analyse_data(file, country):

	covid_df = pd.read_csv(file)

	covid_df = covid_df[(covid_df['location']==f'{country}') & (covid_df['new_cases']>0)]
	covid_plot = covid_df['new_cases']
	covid_plot.index = np.arange(0, len(covid_plot))
	ax = covid_plot.plot(kind='line', title = f'{country}')
	ax.set_xlabel("Days since first case")
	ax.set_ylabel("New cases")
	plt.show()

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument('-d', '--data_file', help='Name of CSV file containing data.', required= True)
	parser.add_argument('-c', '--country', help='Country for the statistic', required=True)

	args = parser.parse_args()

	analyse_data(args.data_file, args.country)
