# pip install flask
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return "Hello World!"


def test():
    user = request.values.get("user") if request.values.get("user") else 'admin'

    if request.method == 'GET':
        kwargs = {"name": user}
        return render_template('test.html', **kwargs)

    elif request.method == 'POST':
        return {"type": "json", "name": user}


@app.before_request
def before_request():
    print('before_request')


if __name__ == '__main__':
    print(app.view_functions)
    print(app.url_map)

    app.add_url_rule(rule='/test', endpoint='test', view_func=test, methods=["GET", "POST"])

    app.run(host='0.0.0.0', port=8080, debug=True)


