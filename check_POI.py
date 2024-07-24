import sqlite3
from geopy.distance import geodesic
from localisation import get_geolocation, get_public_ip

def get_pois():
    conn = sqlite3.connect('poi.db')
    cursor = conn.cursor() 
    
    cursor.execute('SELECT name, latitude, longitude FROM poi')
    pois = cursor.fetchall()
    
    conn.close()
    return pois

def is_near_poi(current_coords, poi_coords, threshold=100):
    distance = geodesic(current_coords, poi_coords).meters
    print(current_coords, poi_coords)
    return distance <= threshold

def check_nearby_pois(current_coords):
    pois = get_pois()
    for poi in pois:
        name, latitude, longitude = poi
        poi_coords = (latitude, longitude)
        if is_near_poi(current_coords, poi_coords):
            print(f"Vous êtes près de {name}")
            trigger_presentation(name)

def trigger_presentation(poi_name):
    # Cette fonction enverra une requête au LLM avec le nom du POI
    print(f"Présentation du {poi_name}")

if __name__ == "__main__":
    public_ip = get_public_ip()
    if public_ip:
        location_info = get_geolocation(public_ip)
        if 'Latitude' in location_info and 'Longitude' in location_info:
            current_coords = (location_info['Latitude'], location_info['Longitude'])
            print(current_coords)
            check_nearby_pois(current_coords)
        else:
            print("Could not retrieve coordinates from geolocation info")
    else:
        print("Could not retrieve public IP address")

    
    check_nearby_pois(current_coords)