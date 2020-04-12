from flask import Flask, Response, redirect, render_template, request, url_for

app = Flask(__name__)
@app.route("/")
def index():
    # return the rendered template
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host=args["ip"], port=args["port"], debug=True,
        threaded=True, use_reloader=False)
