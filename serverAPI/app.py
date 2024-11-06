from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    try:
        result = float(num1) + float(num2)
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
