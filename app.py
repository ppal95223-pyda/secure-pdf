from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


# ---------------- Home Page ----------------
@app.route("/")
def home():
    return render_template("home.html")


# ---------------- Subject Page ----------------
@app.route("/subject/<subject_name>")
def subject(subject_name):
    return render_template("subject.html", subject=subject_name)


# ---------------- Unit Details Page ----------------
@app.route("/subject/<subject_name>/unit/<int:unit_number>")
def unit(subject_name, unit_number):

    conn = sqlite3.connect("database/notes.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT subject, unit, price, pages, description
        FROM notes
        WHERE subject=? AND unit=?
        """,
       (subject_name.title(), f"Unit {unit_number}")
    )

    # Temporary Debugging
    print("Searching Subject:", subject_name)
    print("Searching Unit:", f"Unit {unit_number}")

    note = cursor.fetchone()

    print("Found:", note)

    conn.close()

    if note:
        return render_template(
            "unit.html",
            subject=note[0],
            unit=note[1],
            price=note[2],
            pages=note[3],
            description=note[4]
        )

    return "Note not found!"


# ---------------- Run App ----------------
if __name__ == "__main__":
    app.run(debug=True)