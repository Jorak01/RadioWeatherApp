import serial
import requests

# Configuration
BAOFENG_PORT = 'COM8'  # Replace with your serial port
BAOFENG_BAUDRATE = 9600
Frequency = 162.400


def fetch_baofeng_data():
    with serial.Serial(BAOFENG_PORT, BAOFENG_BAUDRATE) as ser:
        # Read data from the Baofeng UV-5R8W
        data = ser.readline().decode('utf-8').strip()
        return data


def fetch_weather_data():
    latitude = '30.4927'  # Cedar Park latitude
    longitude = '-97.6740'  # Cedar Park longitude
    api_key = ''

    url = 'https://api.tomorrow.io/v4/weather/forecast?location={latitude},{longitude}&apikey={api_key}'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        current_weather = data['current']
        print(f"Current weather in Austin, TX:")
        print(f"Temperature: {current_weather['temp']}K")
        print(f"Humidity: {current_weather['humidity']}%")
        print(f"Weather: {current_weather['weather'][0]['description']}")
        return response.json() & data.json()
    else:
        return None


def main():
    baofeng_data = fetch_baofeng_data()
    weather_data = fetch_weather_data()

    if weather_data & baofeng_data:
        print("Weather Data:")
        print(weather_data)
        print("Baofeng Data:")
        print(baofeng_data)
    elif baofeng_data:
        print("Baofeng Data:")
        print(baofeng_data)
    elif weather_data:
        print("weather_data:")
        print(weather_data)
    else:
        print("Failed to retrieve weather or Baofeng data.")


if __name__ == '__main__':
    main()
