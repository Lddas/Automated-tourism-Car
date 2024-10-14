# DeloreAI Tourism-Car 

Welcome to the DeloreAI repository ! DeloreAI is a first implementation of a project developped in 24h in the context of the 2024 Infosys BIZHACKATHON in Bangalore. The name of the project is a reference to the classic movie "Back to the future", in which they are driving the futuristic Delorean car. The goal of the concept is to developp a smart and autonous tourist car, that drives the user around, answers the questions, and explains important facts about points of interest.
In this code, we implemented a first draft of the detection of the points of interest in the campus, as the car is passing in front of them. For this, we use a Google Maps API.


Let's implement an autonomous tourism tour car ! This code is implemented as an @app. 

It detects dynamically (checks every 5sec) the car position thanks to the html file.
Then, it compares the localisation to the implemented Points of Interest (POI). Here, we implememented some of the campus musts, like the Washing Machine building.
All the POIs are implemented in a SQLite database. 

If you want to try it, run app.py, and copy the link "http://127.0.0.1:5000" on your browser, for it to find your localisation.


