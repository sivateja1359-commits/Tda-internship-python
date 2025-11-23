import requests

def get_weather(city, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"].title(),
        }
        return weather

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Network error: {err}")
    except KeyError:
        print("Unexpected data format received from API.")
    return None


def main():
    print("=== Simple Weather App ===")
    api_key = input("Enter your OpenWeatherMap API Key: ").strip()
    city = input("Enter city name: ").strip()

    print("\nFetching weather...")

    weather = get_weather(city, api_key)

    if weather:
        print("\n🌤️ Weather Report:")
        print(f"City       : {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Feels Like : {weather['feels_like']}°C")
        print(f"Humidity   : {weather['humidity']}%")
        print(f"Condition  : {weather['weather']}")
    else:
        print("Could not fetch weather. Please try again.")

if __name__ == "__main__":
    main()import requests

def get_weather(city, api_key):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"].title(),
        }
        return weather

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Network error: {err}")
    except KeyError:
        print("Unexpected data format received from API.")
    return None


def main():
    print("=== Simple Weather App ===")
    api_key = input("Enter your OpenWeatherMap API Key: ").strip()
    city = input("Enter city name: ").strip()

    print("\nFetching weather...")

    weather = get_weather(city, api_key)

    if weather:
        print("\n🌤️ Weather Report:")
        print(f"City       : {weather['city']}")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Feels Like : {weather['feels_like']}°C")
        print(f"Humidity   : {weather['humidity']}%")
        print(f"Condition  : {weather['weather']}")
    else:
        print("Could not fetch weather. Please try again.")

if __name__ == "__main__":
    main()