from flask import Flask, render_template

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/subject/<subject_name>")
def subject(subject_name):
    return render_template("subject.html", subject=subject_name)

if __name__ == "__main__":
    app.run(debug=True)