from flask import Flask, request, render_template_string

app = Flask(__name__)

html_template = """
<!doctype html>
<title>Simple Calculator</title>
<h2>Calculator App</h2>
<form method="POST">
    Number 1: <input type="number" name="num1" required><br><br>
    Number 2: <input type="number" name="num2" required><br><br>
    Operation:
    <select name="operation">
        <option value="add">Add (+)</option>
        <option value="subtract">Subtract (-)</option>
        <option value="multiply">Multiply (×)</option>
        <option value="divide">Divide (÷)</option>
    </select><br><br>
    <input type="submit" value="Calculate">
</form>

{% if result is not none %}
    <h3>Result: {{ result }}</h3>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operation = request.form['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Error: Divide by zero'

    return render_template_string(html_template, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
