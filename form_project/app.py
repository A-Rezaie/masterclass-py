from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

records = []

@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()

        if not name :
            return "نام نباید خالی باشد", 400

        try:
            age = int(request.form.get("age", ""))
        except ValueError:
            return "سن باید عدد صحیح باشد", 400

        interest = request.form.get("interest")

        try:
            interest_level = int(request.form.get("interest_level", ""))
        except ValueError:
            return "میزان علاقه باید عدد صحیح باشد", 400

        if not 1 <= interest_level <= 10:
            return "میزان علاقه باید بین ۱ تا ۱۰ باشد", 400


        description = request.form.get("description")

        record = {
        "name": name, "age": age, "interest": interest,
        "interest_level": interest_level, "description": description
                 }
        records.append(record)

        print(record)

        return redirect (url_for("index"))

    
    return render_template("index.html", records = records)


if __name__ == "__main__":
    app.run(debug=True)
