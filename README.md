# ✅ **To-Do List Application**

A powerful and clean **Python CLI To-Do Manager** that follows PEP 8, PEP 257, and best engineering practices.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue.svg" />
  <img src="https://img.shields.io/badge/License-MIT-green.svg" />
  <img src="https://img.shields.io/badge/CLI-Interactive-orange.svg" />
  <img src="https://img.shields.io/badge/Type%20Hints-100%25-brightgreen.svg" />
  <img src="https://img.shields.io/badge/PEP%208-Compliant-blueviolet.svg" />
  <img src="https://img.shields.io/badge/PEP%20257-Docstrings-yellow.svg" />
  <img src="https://img.shields.io/badge/Dataclasses-Enabled-lightgrey.svg" />
  <img src="https://img.shields.io/badge/Made%20With-Python🐍-blue.svg" />
</p>

---

# 🌟 Features

## **✔ Core Features**

* Add, view, edit, and delete tasks
* Mark tasks as complete/incomplete
* Set priorities
* Due dates
* Categories
* Descriptions
* Color tags
* Type-safe design
* Clean documentation

---

## 🚀 **Advanced Features**

### Sorting

* By due date
* By priority
* By title
* By category

### Filtering & Search

* Search by title, description, or category
* View only completed / pending tasks

### Analytics

* Total tasks
* Completion rate
* Priority breakdown
* Category breakdown

### Exporting

* CSV
* TXT

---

# 🧱 Technical Overview

## Dataclass Model

```python
@dataclass
class Task:
    title: str
    completed: bool = False
    priority: Priority = Priority.MEDIUM
    due_date: Optional[str] = None
    category: str = "general"
    description: Optional[str] = None
    color: Optional[str] = None
```

## Priority Enum

```python
class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
```

---

# 🚀 Quick Start

## 1️⃣ Clone the repository

```bash
git clone https://github.com/husseini2000/To-Do-List.git
cd todo-app
```

## 2️⃣ Run the app

```bash
python todo.py
```

✔ No external dependencies
✔ Python standard library only

---

# 🧭 Usage (Menu-Based)

When you run the app, you'll see:

```
==============================
        TO-DO LIST MENU
==============================
1. Add a new task
2. View tasks
3. Update a task
4. Delete a task
5. Mark complete/incomplete
6. Sort tasks
7. Search tasks
8. View statistics
9. Export tasks
10. Exit
==============================
```

### Example Task Display

```
1. ❌ 🟡 Buy groceries [personal] 📅 2025-11-15
```

---

# 💾 Data Storage

### Files

```
tasks.json        # Persistent data
.backups/         # Automatic backups
tasks_export.csv  # CSV export
tasks_export.txt  # Text export
```

### Features

* JSON-based storage
* Automatic timestamped backups
* Corruption recovery

---

# 🧪 Code Quality

<p align="left">
  <img src="https://img.shields.io/badge/Code%20Style-PEP8-blue.svg" />
  <img src="https://img.shields.io/badge/Type%20Hints-Strict-brightgreen.svg" />
  <img src="https://img.shields.io/badge/Code-Documented-yellow.svg" />
  <img src="https://img.shields.io/badge/Errors-Handeled-red.svg" />
</p>

---

# 🛠 Future Enhancements

* Multiple lists
* Subtasks
* Reminders
* Recurring tasks
* Collaboration
* AI prioritization
* Charts and graphics
* Template-based tasks
* Dependencies

---

# 🤝 Contributing

<details>
<summary><strong>Contribution Guidelines</strong></summary>

1. Follow PEP 8
2. Use type hints consistently
3. Write clear PEP 257 docstrings
4. Add tests when possible
5. Update documentation

</details>

---
# 🧑‍💻 Author

**Al-Husseini Ahmed Abdelaleem**
<p align="center">
  <a href="mailto:husseiniahmed2015@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-Email-red?style=flat&logo=gmail" />
  </a>
  <a href="www.linkedin.com/in/al-husseinirayan/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin" />
  </a>
</p>
---

# 📄 License

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" />
</p>

This project is licensed under the **MIT License**.
