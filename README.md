# 🎓 Student Management System

A simple **console-based Student Management System** built with Python. It lets you add multiple students, enter their subject-wise marks, and automatically calculates totals, percentages, and letter grades.

---

## ✨ Features

- Add student with any number of subjects
- Input validation (only integers, marks between 0–100)
- Auto-calculates total, percentage, and grade
- View result cards for all students
- Clean modular code with separate functions

---

## 🗂️ Project Structure

```
student-management-system/
│
├── main.py        # Main application file
└── README.md      # Project documentation
```

---

## ▶️ How to Run

Make sure you have **Python 3** installed.

```bash
python main.py
```

---

## 📋 Menu Options

| Option | Action              |
|--------|---------------------|
| 1      | Add a new student   |
| 2      | Show all students   |
| 3      | Exit the program    |

---

## 📊 Grading Criteria

| Percentage | Grade |
|------------|-------|
| 90% – 100% | A     |
| 80% – 89%  | B     |
| 70% – 79%  | C     |
| 60% – 69%  | D     |
| Below 60%  | F     |

---

## 💡 Example Output

```
===== Student Management System =====
1. Add Student
2. Show All Students
3. Exit
Enter your choice: 1

Enter your name: Hassan
Enter number of subjects: 3
Enter marks for subject 1: 85
Enter marks for subject 2: 92
Enter marks for subject 3: 78

Student 'Hassan' added successfully!

----- RESULT -----
Name:       Hassan
Marks:      [85, 92, 78]
Total:      255
Percentage: 85.00%
Grade:      B
------------------
```

---

## 🛠️ Built With

- Python 3 (no external libraries required)

---
