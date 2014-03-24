# FLEX EYE Data Parsing 
# Data file can be found out at : http://archive.ics.uci.edu/ml/machine-learning-databases/00235/household_power_consumption.zip
# Optimisation method used is Nelder-Mead 

import numpy as np
from scipy.optimize import minimize

DataFile = open("house_data.dat","rb") 
DataFile.readline()
LineCount = 1
DailyConsumption = [0.0,0.0,0.0]
HourlyConsumption = [0.0,0.0,0.0]
DailyBook = {}
HourlyBook = {}
Hours = 0

DailyMeterData = []
HourlyMeterData = []

#Consumption Date and Time, SubMeter(1,2,3)
for line in DataFile:
	Data = line.split(';')

	#DailyConsumption
	if(LineCount % 1440 == 1):
		DailyBook[Data[0]] = DailyConsumption
		DailyConsumption = [0.0,0.0,0.0]
	try:
		DailyConsumption[0] = DailyConsumption[0] + float(Data[6]) 
		DailyConsumption[1] = DailyConsumption[1] + float(Data[7]) 
		DailyConsumption[2] = DailyConsumption[2] + float(Data[8].strip()) 
	except:
		continue

	#HourlyConsumption
	if(Hours < 24):
		if(LineCount % 60 == 1):
			HourlyBook[Data[1]] = HourlyConsumption
			HourlyConsumption = [0.0,0.0,0.0]
			Hours = Hours + 1
		try:
			HourlyConsumption[0] = HourlyConsumption[0] + float(Data[6]) 
			HourlyConsumption[1] = HourlyConsumption[1] + float(Data[7]) 
			HourlyConsumption[2] = HourlyConsumption[2] + float(Data[8].strip()) 
		except:
			continue

	LineCount = LineCount +1

for data in DailyBook:
	#print data,DailyBook[data]
	DailyMeterData.append(DailyBook[data][0]+ DailyBook[data][1] + DailyBook[data][2])
for data in HourlyBook:
	#print data,HourlyBook[data]
	HourlyMeterData.append(HourlyBook[data][0]+ HourlyBook[data][1] + HourlyBook[data][2])

#Optimisation
def rosen(x):
	"""The Rosenbrock function"""
	return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

x0 = np.array(HoulryMeterData)
x1 = np.array(DailyMeterData)
res0 = minimize(rosen, x0, method='nelder-mead',options={'xtol': 1e-8, 'disp': True})
res1 = minimize(rosen, x1, method='nelder-mead',options={'xtol': 1e-8, 'disp': True})

print res0.x
print res1.x

