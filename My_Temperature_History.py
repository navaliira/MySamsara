import json
import requests
import matplotlib.pyplot as plt
from datetime import datetime
"""
Input parameters; e.g. API Token, groupId, baseUrl, etc.
"""
access_token = '8lRABQGYyah8lpcvB2r1uGk4FYkkUN'
groupId = 33959
baseUrl = 'https://api.samsara.com/v1'
sensorId_Door = 212014918372977
sensorId_Environment = 212014918414714
fill_missing = "withNull"


#Required Time Span
##############################
# From 17 June 2019, 00:00:00
startMs = 1560729600000
# To 20 June 2019, 00:00:00
endMs = 1560988800000
#With Increments
stepMs = 14400000


#Required Result Field
##############################
series = [{"widgetId": sensorId_Environment, "field": "ambientTemperature"}]

"""
Response Codes Descriptions
"""
def responseCodes(response):
	"""
	This function performs error handling for the API calls.
	"""
	if response.status_code >= 200 and response.status_code < 299:
	#Do nothing, API call was successful
		pass
	elif response.status_code == 400:
		print(response.text)
		raise ValueError('Bad Request: Please make sure the request follows the format specified in the documentation.')
	elif response.status_code == 401:
		print(response.text)
		raise ValueError('Invalid Token: Could not authenticate successfully')
	elif response.status_code == 404:
		print(response.text)
		raise ValueError('Page not found: API Endpoint is invalid')
	else:
		print(response.text)
		raise ValueError('Request was not successful')

		
"""
Extracting the temperature history from the Environment sensor within specific times       
"""
def getSensorsHistory(access_token,groupId):
	sensorsHistoryUrl = '/sensors/history'
	parameters = {"access_token":access_token}

	requestBodyTemperature = {
			"endMs": endMs,
			"fillMissing": fill_missing,
			"groupId": groupId,
			"series": [
				{
				"field": "ambientTemperature",
				"widgetId": sensorId_Environment
				}
			],
			"startMs": startMs,
			"stepMs": stepMs
		}

	response = requests.get(baseUrl+sensorsHistoryUrl,params=parameters,json=requestBodyTemperature)

	responseCodes(response)
	return response.json()['results']

##Saving Result
Result = getSensorsHistory(access_token,groupId)

"""
Plotting Result in real time format
"""
x_timeMs = [i['timeMs'] for i in Result if 'timeMs' in i]
x_realTime = [datetime.utcfromtimestamp(j/1000).strftime('%m/%d   %H:%M:%S') for j in x_timeMs]
y_temperature = [i['series'][0]/1000 for i in Result if 'series' in i]

plt.plot(x_realTime, y_temperature)
plt.xticks(x_realTime, rotation='vertical')
plt.title("Temperature History")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.grid(color='g', linestyle='-', linewidth=0.1)
plt.show()
