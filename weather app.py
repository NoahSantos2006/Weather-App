from bs4 import BeautifulSoup
import requests
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent='weather app')
while True:
    user_input = input("Type 'exit' to exit the application. Otherwise, a location: ")
    print()
    if 'exit' in user_input:
        print('Have a nice day!\n')
        exit()
    else:
        try:

            print()

            location = lambda query: geolocator.geocode("%s, United States" % query)

            latitude = location(user_input).latitude
            longitude = location(user_input).longitude
            
            url = f"https://forecast.weather.gov/MapClick.php?lat={latitude}&lon={longitude}"

            page = requests.get(url).text

            soup = BeautifulSoup(page, "html.parser")

            office = soup.find('h3', id = "getfcst-headOffice").text.strip()

            currentDegreesF = soup.find('p', class_ = 'myforecast-current-lrg').text.strip()

            conditions = soup.find_all('table')

            for value in conditions:
                conditions1 = value.find_all('b')
                conditions2 = value.find_all('td', class_= None)

            conditionsTotal = dict(zip([value.text.strip() for value in conditions1], [value.text.strip() for value in conditions2]))


            print(f"Your local forecast office is in {office}\n")

            print(f"It is currently: {currentDegreesF}\n")

            for key, value in conditionsTotal.items():
                print(f"{key}: {value}")

            print()

        except:
            print("I couldn't find that location.\n")

