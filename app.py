from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")


# Subject Page
@app.route("/subject/<subject_name>")
def subject(subject_name):
   return render_template("subject.html", subject=subject_name)


# Unit Details Page
@app.route("/subject/<subject_name>/unit/<int:unit_number>")
def unit(subject_name, unit_number):
    return render_template(
        "unit.html",
        subject=subject_name,
        unit=unit_number,
        price=49,
        description="Complete notes with diagrams."
    )


if __name__ == "__main__":
    app.run(debug=True)