from flask import Flask,render_template


app = Flask(__name__)


JOBS = [
    {
        "id":1,
        "title":"web developer",
        "salary":100000,
    },
    {
        "id":2,
        "title":"android developer",
        "salary":150000,
    },
    {
        "id":3,
        "title":"python developer",
        "salary":120000,
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html",jobs=JOBS)



if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)