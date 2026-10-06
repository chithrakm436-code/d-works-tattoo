

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)

# Allow frontend to connect with backend
CORS(app)


# Home API
@app.route("/")
def home():
    return "Welcome to D works Tattoo Backend!"


# Shop information API
@app.route("/api/shop")
def shop():

    shop_details = {
        "name": "D works Tattoo",
        "location": "Attibele",
        "artist": "Deepak",

        "tattoo_types": [
            "Portrait",
            "Mandala Art",
            "Colouring",
            "Black and Grey",
            "Realism"
        ],

        "services": [
            "Tattoos",
            "Paintings",
            "Pencil Sketching"
        ],

        "starting_price": 1000,

        "instagram": "@_d_works_tattoo",

        "phone": "6361918038",

        "email": "deepakdeepu3545@gmail.com",

        "about": "We provide good tattoo services while maintaining proper hygiene and a clean environment."
    }

    return jsonify(shop_details)

@app.route("/images/<filename>")
def serve_image(filename):
    image_folder = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "frontend",
        "images"
    )

    return send_from_directory(image_folder, filename)

# Tattoo images API
@app.route("/api/images")
def images():

    image_folder = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "frontend",
        "images"
    )

    image_files = []

    for file in os.listdir(image_folder):
        if file.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            image_files.append(file)

    return jsonify(image_files)


# Start the server
if __name__ == "__main__":
    app.run(debug=True)