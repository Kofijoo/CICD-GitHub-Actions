from flask import Flask, jsonify, request

from app.calculator import calculate_expression, calculate_operation

app = Flask(__name__)


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()

    # Handle expression mode
    if "expression" in data:
        try:
            result = calculate_expression(data["expression"])
            return jsonify({"result": result})
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    # Handle structured operation mode
    elif all(k in data for k in ("a", "b", "operation")):
        try:
            result = calculate_operation(data["a"], data["b"], data["operation"])
            return jsonify({"result": result})
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return jsonify({"error": "Invalid input format"}), 400


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    app.run(debug=True)
