import json
import requests

"""
Input parameters; e.g. API Token, groupId, baseUrl, etc.
"""
access_token = '8lRABQGYyah8lpcvB2r1uGk4FYkkUN'
groupId = 33959
baseUrl = 'https://api.samsara.com/v1'
sensorId_Environment = 212014918414714


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
Extracting the current humidity info from the Environment sensor        
"""
def getSensorsHumidity(access_token,groupId):
	sensorsHumidityUrl = '/sensors/humidity'

	parameters = {"access_token":access_token}

	requestBody= {
					"groupId": groupId,
					"sensors": [sensorId_Environment]
				}

	response = requests.get(baseUrl+sensorsHumidityUrl,params=parameters,json=requestBody)

	responseCodes(response)
	return response.json()['sensors']

#Saving Result only as a dictionary
Result = getSensorsHumidity(access_token,groupId)[0]

#Display of Humidity
print("Current Humidity = ",Result['humidity'], " %")
