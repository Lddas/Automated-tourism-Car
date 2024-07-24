from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_location', methods=['POST'])
def save_location():
    data = request.get_json()
    lat = data['latitude']
    lng = data['longitude']
    print(f"Received location: Latitude = {lat}, Longitude = {lng}")
    # You can now use the coordinates in your Python code
    # For example, save to a database, call another function, etc.
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
