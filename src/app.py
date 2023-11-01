from random import randint

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data = int(open("data.txt").read())
    data += 1
    open("data.txt", "w").write(str(data))
    chosen_image = randint(0, 9)
    return render_template("index.html", number=data,
                           image=f"{chosen_image}.jpg")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
