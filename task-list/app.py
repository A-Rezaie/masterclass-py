from flask import Flask, render_template, request, redirect, Response
import openpyxl
import json

app = Flask(__name__)

with open("tasks.json", "r") as file:
    tasks = json.load(file)
    if tasks:
        next_id = max(task["id"] for task in tasks) + 1
    else:
        next_id = 1


@app.route("/", methods=["GET", "POST"])
def index():
    global next_id

    if request.method == "POST":

        excel_file = request.files.get("excel")
        if excel_file:
            workbook = openpyxl.load_workbook(excel_file)
            sheet = workbook.active
            for row in sheet.iter_rows(values_only=True, min_row=2):
                title, description, status = row
                task = {
                    "title": title,
                    "description": description,
                    "status": status,
                    "id": next_id,
                }
                tasks.append(task)
                next_id += 1

            with open("tasks.json", "w") as file:
                json.dump(tasks, file)

            return redirect("/")

        title = request.form.get("title")
        description = request.form.get("description")
        status = request.form.get("status")
        task = {
            "title": title,
            "description": description,
            "status": status,
            "id": next_id,
        }
        tasks.append(task)
        next_id += 1
        with open("tasks.json", "w") as file:
            json.dump(tasks, file)

        return redirect("/")

    return render_template("index.html", tasks=tasks)


@app.get("/delete/<int:task_id>")
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)

    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

    return redirect("/")


@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            if request.method == "POST":
                title = request.form.get("title")
                description = request.form.get("description")
                status = request.form.get("status")
                task["title"] = title
                task["description"] = description
                task["status"] = status

                with open("tasks.json", "w") as file:
                    json.dump(tasks, file)

                return redirect("/")
            return render_template("edit.html", task=task)
    return redirect("/")


@app.get("/download-json")
def download_json():
    json_data = json.dumps(tasks)
    response = Response(json_data, mimetype="application/json")
    response.headers["Content-Disposition"] = "attachment; filename=tasks.json"
    return response
