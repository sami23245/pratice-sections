from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

# File to store tasks
DATA_FILE = "todos.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

@app.route("/", methods=["GET", "POST"])
def index():
    tasks = load_tasks()
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append({"task": task, "done": False})
            save_tasks(tasks)
        return redirect(url_for("index"))
    return render_template("index.html", tasks=tasks)

@app.route("/toggle/<int:task_id>")
def toggle(task_id):
    tasks = load_tasks()
    tasks[task_id]["done"] = not tasks[task_id]["done"]
    save_tasks(tasks)
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>")
def delete(task_id):
    tasks = load_tasks()
    tasks.pop(task_id)
    save_tasks(tasks)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
