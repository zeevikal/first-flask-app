from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        value_one = int(request.form['first'])
        value_two = int(request.form['second'])
        total = value_one + value_two
        data = {"total": str(total)}
        return jsonify(data)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)