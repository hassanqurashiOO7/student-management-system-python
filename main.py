# ============================================================
# Student Management System
# Description: A console-based app to manage student records.
#              Supports adding students with multi-subject marks,
#              calculating totals, percentages, and grades.
# ============================================================

def get_info():
    """Collect student name and validated subject marks from user input."""
    name = input("Enter your name: ")

    # Keep asking until user gives a valid positive number of subjects
    while True:
        try:
            sbj = int(input("Enter number of subjects: "))
            if sbj <= 0:
                print("Invalid number. Please enter a positive value.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    # Collect marks for each subject with range validation (0–100)
    num_sbj = []
    for i in range(sbj):
        while True:
            try:
                subject_marks = int(input(f"Enter marks for subject {i + 1}: "))
                if 0 <= subject_marks <= 100:
                    num_sbj.append(subject_marks)
                    break
                else:
                    print("Marks must be between 0 and 100. Try again.")
            except ValueError:
                print("Please enter a valid integer.")

    return name, num_sbj


def calsum(num_sbj):
    """Calculate and return the total marks from the list of subject marks."""
    return sum(num_sbj)


def percentage(total, num_sbj):
    """Calculate percentage based on total marks and number of subjects (max 100 each)."""
    return (total / (len(num_sbj) * 100)) * 100


def grades(per):
    """Return letter grade based on percentage score."""
    if per >= 90:
        return "A"
    elif per >= 80:
        return "B"
    elif per >= 70:
        return "C"
    elif per >= 60:
        return "D"
    else:
        return "F"


def display(name, num_sbj, total, per, grade):
    """Print a formatted result card for a single student."""
    print("\n----- RESULT -----")
    print(f"Name:       {name}")
    print(f"Marks:      {num_sbj}")
    print(f"Total:      {total}")
    print(f"Percentage: {per:.2f}%")
    print(f"Grade:      {grade}")
    print("------------------")


def main():
    """Main loop — displays menu and handles user choices."""
    students = {}  # Dictionary to store {name: [marks]} for all students

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Exit")

        choose = input("Enter your choice: ")

        if choose == "1":
            # Get student data and store in dictionary
            name, num_sbj = get_info()
            students[name] = num_sbj
            print(f"Student '{name}' added successfully!")

        elif choose == "2":
            # Display result card for each stored student
            if not students:
                print("No students found.")
            else:
                for name, num_sbj in students.items():
                    total = calsum(num_sbj)
                    per = percentage(total, num_sbj)
                    grade = grades(per)
                    display(name, num_sbj, total, per, grade)

        elif choose == "3":
            print("Exiting program. Goodbye! 👋")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Entry point — only runs when executed directly, not when imported
if __name__ == "__main__":
    main()
