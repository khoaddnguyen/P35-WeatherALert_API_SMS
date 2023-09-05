import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "API keys"  # replace when test run [API Key]
account_sid = "TWILIO_ACCOUNT_SID"  # replace when test run ['TWILIO_ACCOUNT_SID']
auth_token = "TWILIO_AUTH_TOKEN"  # replace when test run ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

weather_params = {
    "lat": 39.22,
    "lon": 22.55,
    "appid": api_key
}

# Ventusky.com provides current weather of locations for handy testing
# Precipitation for raining weather

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
condition_code = weather_data["weather"][0]["id"]

will_rain = True

if int(condition_code) < 700:
    print("Bring ☔️")
else:
    pass

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain. Bring an ☔️",
        from_="Twilio_phone_number",  # Twilio_phone_number
        to="actual phone number"  # actual phone number
    )
    print(message.status)
    print(message.sid)

print(weather_data["weather"][0]["id"])



