import math


def calculate_expression(expression: str):
    try:
        # Very basic safe evaluation using eval and math
        allowed_names = {
            k: v for k, v in math.__dict__.items() if not k.startswith("__")
        }
        return eval(expression, {"__builtins__": {}}, allowed_names)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


def calculate_operation(a, b, operation):
    a = float(a)
    b = float(b)

    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Division by zero")
        return a / b
    elif operation == "power":
        return a**b
    elif operation == "modulo":
        return a % b
    else:
        raise ValueError("Unsupported operation")
