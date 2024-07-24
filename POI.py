import sqlite3

# Connexion à la base de données (ou création de celle-ci)
conn = sqlite3.connect('poi.db')
cursor = conn.cursor()

# Création de la table des POI
cursor.execute('''
    CREATE TABLE IF NOT EXISTS poi (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        latitude REAL NOT NULL,
        longitude REAL NOT NULL
    )
''')

# Quelques POI d'exemple
poi_data = [
    ("La Terrace", 12.850541, 77.665506),  # Exemple : Tour Eiffel
    ("ECC building", 12.850959, 77.665806),  # Exemple : Statue de la Liberté
    ("Washing machine building", 12.849908, 77.666289)  # Exemple : Big Ben
]

# Insertion des POI dans la table
cursor.executemany('''
    INSERT INTO poi (name, latitude, longitude)
    VALUES (?, ?, ?)
''', poi_data)

# Sauvegarde des changements et fermeture de la connexion
conn.commit()
conn.close()

print("POI ajoutés avec succès à la base de données.")