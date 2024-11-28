# Weather Notification Service

This project fetches real-time weather data for a given city using the OpenWeather API and sends weather updates via SMS using the Twilio API. It periodically fetches weather information and sends an SMS with the weather description and temperature in both Celsius and Fahrenheit.

---

## Features

   - Fetches current weather data for a specified city.
   - Converts temperature from Kelvin to both Celsius and Fahrenheit.
   - Sends SMS notifications with weather updates via Twilio.
   - Logs data for debugging and monitoring.
   - Sends updates at regular intervals (e.g., every 6 hours).

---

## Requirements

   - Python 3.x
   - twilio Python package
   - urllib and json libraries (part of Python standard library)
   - OpenWeather API key (free tier available)
   - Twilio account SID and authentication token

---

## Setup

1. Clone the repository:

```
git clone https://github.com/yourusername/weather-notification.git
cd weather-notification
```

2. Install required packages:

Install Twilio's Python package via pip:

```
pip install twilio
```

3. Set up environment variables:

You need to create an .env file to store sensitive information like your API keys and Twilio credentials. You can manually create the file or use a tool like python-dotenv.

In your .env file, add the following:

```
TWILIO_ACCOUNT_SID="your_twilio_account_sid"
TWILIO_AUTH_TOKEN="your_twilio_auth_token"
OPENWEATHER_API_KEY="your_openweathermap_api_key"
TWILIO_PHONE_NUMBER="your_twilio_phone_number"
RECIPIENT_PHONE_NUMBER="recipient_phone_number"
```

4. Run the script:

Once you’ve set up your environment variables, you can run the script to start receiving periodic weather updates.

```
python weather_notifier.py
```

This will fetch the weather data for the specified city, send an SMS with the weather information, and continue to send updates at regular intervals (6 hours by default).

---

## Code Structure

   - weather_notifier.py: The main script that fetches weather data, formats it, and sends it via Twilio.
   - .env: Environment file to store API keys and sensitive information.
   - logs/: Directory where logs are stored for debugging and monitoring purposes.

---

## Customization

You can modify the following aspects:

   - City: Change the city name in the script to get weather data for a different location.
   - Interval: Modify the time.sleep() function to change the interval between weather updates (currently set to 6 hours).
   - Additional Weather Data: Extend the script to include more weather details like wind speed, humidity, or pressure by extracting additional fields from the OpenWeather API response.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Troubleshooting

    Error in fetching data: Ensure your OpenWeather API key is valid and the city name is correct.
    Twilio message not sent: Check your Twilio account SID, authentication token, and phone numbers.

---

## Future Improvements

    Integrate with a more advanced notification service (e.g., email, push notifications).
    Add more cities and allow users to specify the city dynamically via user input.
    Add a GUI or web interface for easier configuration and monitoring.