# Student Management System 🎓

A modular, console-based **Student Management System** developed in Python. This project demonstrates core programming concepts including advanced data structures, persistent file handling, string manipulation, and analytics.

---

## 👨‍💻 Author
* **Mohamed Wael**

---

## 📌 Project Overview
The application is designed to store, manage, update, and search student records efficiently using a command-line interface. It handles course enrollments dynamically while ensuring data integrity and persistent storage.

---

## ✨ Features

- ➕ **Add New Student:** Create profiles with unique IDs, names, ages, and courses.
- 📋 **View All Students:** Display all registered student profiles in a structured layout.
- 🔍 **Search Functionality:** Flexible case-insensitive search by ID or name using custom string methods.
- ⚙️ **Dynamic Course Management:** Add or remove courses seamlessly while eliminating duplicates using Python `set` operations.
- 🗑️ **Delete Student:** Remove student records by unique ID.
- 💾 **Automatic Data Persistence:** Loads records automatically upon startup and saves all updates back to `students.txt`.
- 📊 **Course Enrollment Analytics:** Aggregate and display overall student counts enrolled per subject.
- 📁 **Export to CSV:** Export the student database directly into standard `students_export.csv` files.

---

## 🛠️ Tech Stack & Concepts Applied

- **Language:** Python 3.x
- **Data Structures:** 
  - `Dictionaries` (Main database storage)
  - `Tuples` (Immutable initial course structure)
  - `Sets` (Duplicate prevention during course updates)
- **Built-in Modules:** `csv`, `os`
- **File I/O:** Text file parsing (`|` delimited) and standard CSV exporting.

---

## 🚀 Getting Started

### Prerequisites
* Make sure you have **Python 3.x** installed on your machine.

### Installation & Execution
