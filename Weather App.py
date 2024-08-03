import serial
import requests

# Configuration
BAOFENG_PORT = 'COM8'  # Replace with your serial port
BAOFENG_BAUDRATE = 9600
WEATHER_API_KEY = '4e4cccd3d1044fcca6441813240308'
WEATHER_API_URL = 'https://api.weather.com/v3/wx/conditions/current?apiKey={}&geocode={}&format=json'


def fetch_baofeng_data():
    with serial.Serial(BAOFENG_PORT, BAOFENG_BAUDRATE) as ser:
        # Read data from the Baofeng UV-5R8W
        data = ser.readline().decode('utf-8').strip()
        return data


def fetch_weather_data():
    latitude = '30.4927'  # Cedar Park latitude
    longitude = '-97.6740'  # Cedar Park longitude
    url = WEATHER_API_URL.format(WEATHER_API_KEY, f'{latitude},{longitude}')

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def main():
    baofeng_data = fetch_baofeng_data()
    weather_data = fetch_weather_data()

    if weather_data:
        print("Weather Data:")
        print(weather_data)
    elif baofeng_data:
        print("Baofeng Data:")
        print(baofeng_data)
    else:
        print("Failed to retrieve weather or Baofeng data.")


if __name__ == '__main__':
    main()
