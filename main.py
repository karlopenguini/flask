from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)
model = pickle.load(open('model.sav','rb'))

@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})
@app.route('/predict', methods=["POST"])
def predict():
    
    data = request.json  # Get input data from the request
    dict = {
        0:"Home Maintenance Enthusiasts",
        1:"Family-Centric Homeowners",
        2:"Active & Independent Residents",
        3:"Young & Energetic Urban Dwellers",
        4:"Family-Centric Budgeters",
        5:"Elite & Well-Established Homeowners",
    }

    
    return jsonify({"predictedHomeowner":data})



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
