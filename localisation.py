import requests

def get_public_ip():
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code == 200:
        return response.json()['ip']
    else:
        return None

def get_geolocation(ip, access_token):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{ip}.json"
    params = {
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        location_data = response.json()
        return location_data
    else:
        return None

if __name__ == "__main__":
    access_token = 'pk.eyJ1IjoibGVvZGFzIiwiYSI6ImNseXpyN3J6NzJvamkycXM2eGpvMDk4NjYifQ.NWRQ4D3n29LObXaVJo0G0w'
    ip = get_public_ip()
    if ip:
        location_info = get_geolocation(ip, access_token)
        if location_info:
            # Extracting coordinates from the response
            features = location_info.get('features')
            if features and len(features) > 0:
                coordinates = features[0]['geometry']['coordinates']
                lat, lon = coordinates[1], coordinates[0]
                current_coords = (lat, lon)
                print(f"Latitude: {lat}, Longitude: {lon}")
            else:
                print("Could not retrieve coordinates from geolocation info")
        else:
            print("Could not retrieve location data")
    else:
        print("Could not retrieve public IP address")
