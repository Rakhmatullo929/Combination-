import itertools
from flask import Flask, request, render_template_string

app = Flask(__name__)


def generate_combinations_html(n):
    symbols = ['+', '-']
    combinations = list(itertools.product(symbols, repeat=n))

    tables_html = ""
    for idx, combo in enumerate(combinations, 1):
        html = f"<h3 style='font-family: Arial, sans-serif; color: #333;'>Table {idx}</h3>"
        html += "<table style='border: 1px solid #ccc; border-collapse: collapse; width: 50%; margin: 10px auto; font-family: Arial, sans-serif; text-align: center; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);'>"
        html += "<thead style='background-color: #f4f4f4;'>"
        html += "<tr>"
        for i in range(1, n + 1):
            html += f"<th style='padding: 10px; border: 1px solid #ddd;'>Column {i}</th>"
        html += "</tr>"
        html += "</thead>"

        html += "<tbody>"
        html += "<tr style='background-color: #fff;'>"
        for symbol in combo:
            html += f"<td style='padding: 10px; border: 1px solid #ddd;'>{symbol}</td>"
        html += "</tr>"
        html += "</tbody>"
        html += "</table>"

        tables_html += html

    return tables_html


TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
    <title>Combinations Generator</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f9f9f9; margin: 0; padding: 20px; text-align: center; }
        h1 { color: #444; }
        form { margin: 20px; }
        input, button { padding: 10px; font-size: 16px; }
        .container { margin-top: 20px; }
    </style>
</head>
<body>
    <h1>Generate Combinations of '+' and '-'</h1>
    <form method="POST">
        <label for="number">Enter a number:</label>
        <input type="number" name="number" id="number" min="1" required>
        <button type="submit">Generate</button>
    </form>
    <div class="container">
        {{ tables|safe }}
    </div>
</body>
</html>
"""


@app.route('/', methods=['GET', 'POST'])
def index():
    tables = ""
    if request.method == 'POST':
        n = int(request.form['number'])
        tables = generate_combinations_html(n)
    return render_template_string(TEMPLATE, tables=tables)


if __name__ == '__main__':
    app.run(debug=True)
