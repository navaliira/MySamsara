import json
import requests

"""
Input parameters; e.g. API Token, groupId, baseUrl, etc.
"""
access_token = '8lRABQGYyah8lpcvB2r1uGk4FYkkUN'
groupId = 33959
baseUrl = 'https://api.samsara.com/v1'


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
Find Sensor(s) Info
"""
def getSensorsList(access_token,groupId):
	# Identifying Sensors
	sensorsListUrl = '/sensors/list'
	parameters = {"access_token":access_token}
	requestBody = {"groupId":groupId}
	response = requests.get(baseUrl+sensorsListUrl,params=parameters,json=requestBody)
	
	responseCodes(response)
	
	return response.json()['sensors']

print(getSensorsList(access_token,groupId))
