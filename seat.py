#overview bus layout
from flask import Flask, render_template

app = Flask(__name__)

# Sample data for buses
buses = [
    {"id": 1, "name": "Bus A", "seats": ["A1", "A2", "A3", "A4", "A5"]},
    {"id": 2, "name": "Bus B", "seats": ["B1", "B2", "B3", "B4", "B5"]},
    {"id": 3, "name": "Bus C", "seats": ["C1", "C2", "C3", "C4", "C5"]},
]

@app.route('/')
def index():
    return render_template('index.html', buses=buses)

if __name__ == '__main__':
    app.run(debug=True)

