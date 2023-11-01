from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    data = int(open("data.txt").read())
    data += 1
    open("data.txt", "w").write(str(data))
    return render_template("index.html", number = data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)