import sqlite3
from geopy.distance import geodesic

def get_pois():
    conn = sqlite3.connect('poi.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT name, latitude, longitude FROM poi')
    pois = cursor.fetchall()
    
    conn.close()
    return pois

def is_near_poi(current_coords, poi_coords, threshold=50):
    distance = geodesic(current_coords, poi_coords).meters
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
    # Exemple de coordonnées actuelles (latitude, longitude)
    current_coords = (12.850546, 77.665467)  # Remplacez par vos coordonnées actuelles
    
    check_nearby_pois(current_coords)