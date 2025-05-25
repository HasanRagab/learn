## 🧠 One-Week To-Do App Challenge

**Tech**: HTML + CSS + Plain Python (no frameworks)
**Storage**: Starts with `JSON` → upgrades to `SQLite`
**Goal**: Understand how the web works from the ground up.

---

### 📁 Folder Structure Over Time

#### 📅 Day 1–2

```
todo-app/
├── index.html
├── style.css
└── server.py
```

#### 📅 Day 3–4

```
todo-app/
├── index.html
├── style.css
├── server.py
└── data/
    └── tasks.json
```

#### 📅 Day 5–7

```
todo-app/
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── core/
│   ├── db.py
│   └── logic.py
├── tasks.db
├── server.py
└── README.md
```

---

## 🗓️ Day-by-Day Breakdown

---

### 📅 **Day 1 – HTML & CSS UI**

* Build static `index.html`:

  * Input field for tasks
  * Task list container
* Style it with `style.css`
* No Python yet — just frontend

---

### 📅 **Day 2 – Run a Local Web Server**

* Use Python's built-in `http.server` module

  ```bash
  python -m http.server
  ```
* Serve `index.html` and `style.css`
* Make sure form submits correctly (it can redirect for now)

---

### 📅 **Day 3 – Handle Form Submission in Python**

* Replace `http.server` with a custom `server.py` using `http.server.BaseHTTPRequestHandler`
* Parse POST requests manually
* Store tasks in `tasks.json`
* Reload task list from JSON on each request

---

### 📅 **Day 4 – Show Tasks on the Page**

* Read tasks from `tasks.json`
* Dynamically generate the HTML with Python (`server.py` outputs full HTML page)
* Show all tasks on page load

---

### 📅 **Day 5 – Add Complete/Delete Task Logic**

* Use buttons or links to:

  * Mark task as complete
  * Delete task
* Handle those actions in Python by modifying the JSON file
* Add timestamp to each task

---

### 📅 **Day 6 – Move to SQLite**

* Replace `tasks.json` with `tasks.db`
* Use Python’s `sqlite3` module
* Create a `core/db.py` with:

  * `add_task()`
  * `get_tasks()`
  * `delete_task()`
  * `mark_complete()`
* Replace all file-based logic with DB queries

---

### 📅 **Day 7 – Final Polish + Share**

* Polish HTML & CSS
* Improve layout and readability
* Add README with:

  * Features
  * How to run
* Push to GitHub
* Optional: Deploy with Replit or PythonAnywhere (console + files only)

---

### ✅ What They’ll Learn

* How basic web servers work
* HTTP requests (GET/POST)
* Serving and handling HTML from Python
* Storing data in JSON
* Working with SQLite databases
* Structuring a growing project

---

