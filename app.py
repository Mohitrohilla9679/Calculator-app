from flask import Flask, render_template, request

app = Flask(__name__)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    error_message = None

    if request.method == "POST":
        num1 = request.form.get("num1", "")
        num2 = request.form.get("num2", "")
        operation = request.form.get("operation", "")

        # Validate input values
        if not is_float(num1) or not is_float(num2):
            error_message = "Please enter valid numbers."
        else:
            num1 = float(num1)
            num2 = float(num2)

            if operation == "add":
                result = add(num1, num2)
            elif operation == "subtract":
                result = subtract(num1, num2)
            elif operation == "multiply":
                result = multiply(num1, num2)
            elif operation == "divide":
                result = divide(num1, num2)

    return render_template("index.html", result=result, error_message=error_message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)