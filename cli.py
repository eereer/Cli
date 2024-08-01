import phonenumbers
from phonenumbers import carrier, geocoder
from opencage.geocoder import OpenCageGeocode

def track_phone_number(phone_number, api_key):
    try:
        number = phonenumbers.parse(phone_number)
        location = geocoder.description_for_number(number, 'en')
        service = carrier.name_for_number(number, 'en')

        query = str(location)
        results = OpenCageGeocode(api_key).geocode(query)

        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']

        print(f"Phone Number: {phone_number}")
        print(f"Location: {location}")
        print(f"Service: {service}")
        print(f"Latitude: {lat}")
        print(f"Longitude: {lng}")

        open_map = input("Do you want to open the location in Google Maps? (yes/no): ")
        if open_map.lower() == "yes":
            import webbrowser
            url = f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"
            webbrowser.open(url)

    except Exception as e:
        print(f"Error: {e}")

def main():
    api_key = input("Enter your OpenCage API key: ")
    phone_number = input("Enter the phone number to track (with country code): ")
    track_phone_number(phone_number, api_key)

if __name__ == "__main__":
    main()