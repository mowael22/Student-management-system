import csv
import os

FILE_NAME = "students.txt"
CSV_FILE_NAME = "students_export.csv"

# Main data structure (Dictionary)
students = {}


def load_data():
    """Load student data from file on application startup."""
    if not os.path.exists(FILE_NAME):
        return

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) == 4:
                    s_id, name, age, courses_str = parts
                    courses = tuple(courses_str.split(",")) if courses_str else ()
                    students[s_id] = {
                        "name": name,
                        "age": int(age),
                        "courses": courses,
                    }
        print("Data loaded successfully!")
    except Exception as e:
        print(f"Error loading data: {e}")


def save_data():
    """Save student data to a text file."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as f:
            for s_id, data in students.items():
                courses_str = ",".join(data["courses"])
                f.write(f"{s_id}|{data['name']}|{data['age']}|{courses_str}\n")
        print("Data saved successfully!")
    except Exception as e:
        print(f"Error saving data: {e}")


def add_student():
    """1. Add a new student."""
    s_id = input("Enter Student ID: ").strip()
    if s_id in students:
        print("Error: Student ID already exists!")
        return

    name = input("Enter Student Name: ").strip()
    try:
        age = int(input("Enter Student Age: "))
    except ValueError:
        print("Error: Please enter a valid integer for age.")
        return

    courses_input = input(
        "Enter courses separated by commas (e.g., Math, Physics): "
    )
    # Using a set to prevent duplicates, then storing as a tuple
    courses_set = {c.strip() for c in courses_input.split(",") if c.strip()}
    courses_tuple = tuple(courses_set)

    students[s_id] = {"name": name, "age": age, "courses": courses_tuple}
    print(f"Student '{name}' added successfully!")


def view_all_students():
    """2. Display all student records."""
    if not students:
        print("No student records found.")
        return

    print("\n--- All Student Records ---")
    for s_id, data in students.items():
        courses_str = ", ".join(data["courses"]) if data["courses"] else "None"
        print(
            f"ID: {s_id} | Name: {data['name']} | Age: {data['age']} | Courses: ({courses_str})"
        )
    print("-" * 30)


def search_student():
    """3. Search for a student by ID or Name using string methods."""
    query = input("Enter Student ID or Name to search: ").strip().lower()
    found = False

    for s_id, data in students.items():
        if (
            s_id.lower().startswith(query)
            or query in data["name"].lower()
            or data["name"].lower().startswith(query)
        ):
            courses_str = ", ".join(data["courses"])
            print(
                f"Found -> ID: {s_id} | Name: {data['name']} | Age: {data['age']} | Courses: ({courses_str})"
            )
            found = True

    if not found:
        print("No matching student records found.")


def update_student():
    """4. Update student courses using set operations."""
    s_id = input("Enter Student ID to update: ").strip()
    if s_id not in students:
        print("Error: Student ID not found!")
        return

    # Convert to set to easily handle add/remove operations without duplicates
    courses_set = set(students[s_id]["courses"])

    print("\n1. Add a Course")
    print("2. Remove a Course")
    choice = input("Select an option (1-2): ").strip()

    if choice == "1":
        new_course = input("Enter course name to add: ").strip()
        if new_course:
            courses_set.add(new_course)
            print(f"Course '{new_course}' added.")
    elif choice == "2":
        rem_course = input("Enter course name to remove: ").strip()
        if rem_course in courses_set:
            courses_set.remove(rem_course)
            print(f"Course '{rem_course}' removed.")
        else:
            print("Course not found in student's profile!")
    else:
        print("Invalid choice.")
        return

    # Save modified courses back as a tuple
    students[s_id]["courses"] = tuple(courses_set)


def delete_student():
    """5. Remove a student record."""
    s_id = input("Enter Student ID to delete: ").strip()
    if s_id in students:
        del students[s_id]
        print(f"Student ID {s_id} removed successfully.")
    else:
        print("Error: Student ID not found!")


def export_to_csv():
    """Extra Challenge: Export database to a CSV file."""
    try:
        with open(CSV_FILE_NAME, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Name", "Age", "Courses"])
            for s_id, data in students.items():
                writer.writerow(
                    [s_id, data["name"], data["age"], ", ".join(data["courses"])]
                )
        print(f"Data exported successfully to '{CSV_FILE_NAME}'!")
    except Exception as e:
        print(f"Error exporting data: {e}")


def course_enrollment_counts():
    """Extra Challenge: Calculate and display enrollment count per course."""
    counts = {}
    for data in students.values():
        for course in data["courses"]:
            counts[course] = counts.get(course, 0) + 1

    if not counts:
        print("No course enrollment data found.")
        return

    print("\n--- Course Enrollment Statistics ---")
    for course, count in counts.items():
        print(f"Course: {course} | Enrolled Students: {count}")
    print("-" * 35)


def main():
    """Main program execution loop."""
    print("====================================")
    print("  STUDENT MANAGEMENT SYSTEM  ")
    print("====================================")

    # Load persistent data at startup
    load_data()

    while True:
        print("\n--- Main Menu ---")
        print("1. Add a New Student")
        print("2. View All Students")
        print("3. Search for a Student")
        print("4. Update Student Information")
        print("5. Delete a Student")
        print("6. Export to CSV File")
        print("7. View Course Enrollment Counts")
        print("8. Save & Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            export_to_csv()
        elif choice == "7":
            course_enrollment_counts()
        elif choice == "8":
            save_data()
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid input! Please choose a number from 1 to 8.")


if __name__ == "__main__":
    main()