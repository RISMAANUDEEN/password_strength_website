from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        password = request.form["password"]
        strength = 0

        if len(password) >= 8:
            strength += 1
        if re.search("[A-Z]", password):
            strength += 1
        if re.search("[a-z]", password):
            strength += 1
        if re.search("[0-9]", password):
            strength += 1
        if re.search("[@#$%!&*]", password):
            strength += 1

        if strength <= 2:
            result = "Weak ❌"
        elif strength <= 4:
            result = "Medium ⚠️"
        else:
            result = "Strong ✅"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
