import sqlite3
from geopy.distance import geodesic

presented_pois = set()

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
        if name in presented_pois:
            continue  # Skip this POI if it has already been presented
        poi_coords = (latitude, longitude)
        if is_near_poi(current_coords, poi_coords):
            print(current_coords, poi_coords)
            print(f"Vous êtes près de {name}")
            trigger_presentation(name)
            presented_pois.add(name)  # Mark this POI as presented

def trigger_presentation(poi_name):
    # Cette fonction enverra une requête au LLM avec le nom du POI
    description = get_poi_description(poi_name)
    if description:
        print(f"Présentation du {poi_name}: {description}")
    else:
        print(f"Présentation du {poi_name}: Description non trouvée")


def get_poi_description(poi_name):
    try:
        with open('poi_descriptions.txt', 'r', encoding='utf-8') as file:
            for line in file:
                name, desc = line.strip().split(':', 1)
                if name.strip() == poi_name:
                    return desc.strip()
    except FileNotFoundError:
        print("Le fichier poi_descriptions.txt n'a pas été trouvé.")
    return None
