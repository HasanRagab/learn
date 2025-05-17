# Introduction to Databases: SQLite

## 📘 What is a Database?

A **database** is an organized collection of data that can be easily accessed, managed, and updated. Databases are used in almost every software system, from mobile apps to large-scale web services.

## 💾 What is SQLite?

**SQLite** is a lightweight, serverless, self-contained SQL database engine. It is widely used for:

- Embedded systems (like mobile apps)
- Local data storage
- Small to medium-sized projects
- Rapid prototyping

### 🔑 Key Features of SQLite

- **Serverless:** No setup or configuration needed.
- **Single file:** All data is stored in one `.sqlite` or `.db` file.
- **Cross-platform:** Works on Windows, Linux, macOS, Android, etc.
- **Zero Configuration:** No server process to install or manage.
- **Standard SQL Support:** Supports most of the SQL-92 standard.
- **Built-in Python support:** (`sqlite3` module)

## 📂 How SQLite Works

- Data is stored in a single file.
- You interact with the database using SQL commands.
- Applications read and write directly to the database file.

## 🛠️ Installing SQLite

### On Ubuntu/Debian

```bash
sudo apt update
sudo apt install sqlite3
```

### On macOS (using Homebrew)

```bash
brew install sqlite
```

### On Windows

- Download from: [https://www.sqlite.org/download.html](https://www.sqlite.org/download.html)
- Extract and add the folder to your system `PATH`.

## 🧪 Basic SQLite Usage

### Creating a Database

```bash
sqlite3 mydatabase.db
```

### Creating a Table

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
```

### Inserting Data

```sql
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');
```

### Querying Data

```sql
SELECT * FROM users;
```

### Exiting SQLite

```sql
.quit
```

## 📚 Resources

- [SQLite Official Website](https://sqlite.org/)
- [SQLite Documentation](https://sqlite.org/docs.html)
- [SQL Tutorial](https://www.w3schools.com/sql/)

---

## 📝 Example: Using in python

```python
import sqlite3
# Connect to SQLite database (or create it)
conn = sqlite3.connect('example.db')
# Create a cursor object
cursor = conn.cursor()
# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)''')
# Insert data
cursor.execute('''
INSERT INTO users (name, email) VALUES (?, ?)''', ('Alice', 'alice@example.com'))
# Commit changes
conn.commit()
# Query data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)
# Close the connection
conn.close()
```

## ✅ Summary

| Feature     | Description                        |
| ----------- | ---------------------------------- |
| Serverless  | No server or configuration needed  |
| Portable    | Entire DB in a single file         |
| Easy to Use | Minimal setup, standard SQL syntax |
| Lightweight | Small binary size, fast operations |

---
