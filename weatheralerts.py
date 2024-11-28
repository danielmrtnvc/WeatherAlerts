import urllib.request
import json

from twilio.rest import Client
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

key = ""
city = "Toronto"
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + key

response = urllib.request.urlopen(url)

parsedData = json.loads(response.read())
desc = parsedData['weather'][0]['description']
temp = parsedData['main']['temp']

customMsg = 'The weather in ' + str(city) + ' is ' + str(int(temp)-273) + 'C and ' + str(desc)
message = client.messages.create(to="", from_="", body=customMsg)