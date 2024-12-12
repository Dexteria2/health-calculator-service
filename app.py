from flask import Flask, request, jsonify
from health_utils import calculate_bmi, calculate_bmr

app = Flask(__name__)

@app.route('/bmi', methods=['POST'])
def bmi():
    data = request.json
    height = data.get('height')
    weight = data.get('weight')

    if not height or not weight:
        return jsonify({"error": "Height and weight are required."}), 400

    try:
        bmi_value = calculate_bmi(float(height), float(weight))
        return jsonify({"BMI": round(bmi_value, 2)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/bmr', methods=['POST'])
def bmr():
    data = request.json
    height = data.get('height')
    weight = data.get('weight')
    age = data.get('age')
    gender = data.get('gender')

    if not height or not weight or not age or not gender:
        return jsonify({"error": "Height, weight, age, and gender are required."}), 400


    try:
        bmr_value = calculate_bmr(float(height), float(weight), int(age), gender.lower())
        return jsonify({"BMR": round(bmr_value, 2)})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)