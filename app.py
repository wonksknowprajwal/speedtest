from flask import Flask, request, redirect, render_template, request
import speedtest
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html", res = "check by clicking")
    else:
        print(request.remote_addr)
        s = speedtest.Speedtest()
        a = s.upload()
        res = s.results.dict()
        return render_template('index.html', res = res)


if __name__ == "__main__":
    app.run()