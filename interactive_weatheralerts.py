import urllib.request
import json
import logging
import time
from twilio.rest import Client

# Set up logging
logging.basicConfig(level=logging.INFO)

# Twilio account SID and auth token
account_sid = "your_account_sid"
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

# OpenWeather API key
key = "your_openweathermap_api_key"
city = "Toronto"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

def get_weather_data():
    try:
        response = urllib.request.urlopen(url)
        parsed_data = json.loads(response.read())
        
        if 'weather' in parsed_data and 'main' in parsed_data:
            description = parsed_data['weather'][0]['description']
            temp_kelvin = parsed_data['main']['temp']
            temp_celsius = int(temp_kelvin - 273.15)  # Convert Kelvin to Celsius
            temp_fahrenheit = int((temp_celsius * 9/5) + 32)  # Convert Celsius to Fahrenheit

            # Log the weather data for debugging purposes
            logging.info(f"Weather in {city}: {description}, Temp: {temp_celsius}C / {temp_fahrenheit}F")

            return temp_celsius, temp_fahrenheit, description
        else:
            logging.error("Error: Weather data is not available")
            return None, None, None
    except Exception as e:
        logging.error(f"Error fetching weather data: {e}")
        return None, None, None

def send_weather_update(temp_celsius, temp_fahrenheit, description):
    if temp_celsius is None:
        logging.error("Weather update not sent due to missing data")
        return

    # Create the message
    custom_msg = f"The weather in {city} is {temp_celsius}°C / {temp_fahrenheit}°F and {description}."
    
    try:
        # Send the weather update via Twilio
        message = client.messages.create(
            to="recipient_phone_number",  # Replace with the recipient's phone number
            from_="your_twilio_number",   # Replace with your Twilio number
            body=custom_msg
        )
        logging.info(f"Weather update sent: {message.sid}")
    except Exception as e:
        logging.error(f"Error sending message: {e}")

# Send weather update every 6 hours (for example)
while True:
    temp_celsius, temp_fahrenheit, description = get_weather_data()
    send_weather_update(temp_celsius, temp_fahrenheit, description)
    time.sleep(21600)  # Sleep for 6 hours (21600 seconds)
