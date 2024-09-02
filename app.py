from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/calculate', methods=['GET'])
def calculate():
    operation = request.args.get('operation')
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    try:
        num1 = float(num1)
        num2 = float(num2)
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

    # Validate operation and calculate result
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = num1 / num2
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result})

@app.route('/random', methods=['GET'])
def generate_random():
    lower = request.args.get('lower', 0)
    upper = request.args.get('upper', 100)
    count = request.args.get('count', 10)

    try:
        lower = int(lower)
        upper = int(upper)
        count = int(count)
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input'}), 400

    if lower > upper:
        return jsonify({'error': 'Lower bound cannot be greater than upper bound'}), 400

    random_numbers = [random.randint(lower, upper) for _ in range(count)]
    return jsonify({'random_numbers': random_numbers, 'result': random.choice(random_numbers)})

if __name__ == '__main__':
    app.run(debug=True)
