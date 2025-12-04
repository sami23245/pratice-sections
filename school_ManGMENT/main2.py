import json
import os

class DataBase:
    def __init__(self):
        self.filepath = r"C:\Users\Samis\OneDrive\Desktop\learning\pratice-sections\school_ManGMENT\school_database.json"

        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r") as f:
                    data = json.load(f)
                    self.students = data.get("students", {})
                    self.Teachers = data.get("teachers", {})
                    self.Admin = data.get("admin", {})
                    self.permissions = data.get("permissions", {})
                    self.programs = data.get("programs", [])
                    self.Scholarships = data.get("Scholarships", {})
                print("✅ Database loaded successfully!")
            except json.JSONDecodeError:
                print("⚠️ Database file corrupted — creating new data.")
                self._create_default_data()
        else:
            print("⚠️ No database found — creating new one.")
            self._create_default_data()

    def _create_default_data(self):
        self.students = {
            "Spc23": {"Name": "Ali", "Class": "9th", "Program": "Science", "Condition": "Great", "Scholarship": "Yes on 80%", "Marks": 98},
            "Spc24": {"Name": "Sara", "Class": "12th", "Program": "ICS", "Condition": "Good", "Scholarship": "No", "Marks": 89},
            "Spc25": {"Name": "Zoro", "Class": "8th", "Program": "Science", "Condition": "Normal", "Scholarship": "Yes on 45%", "Marks": 56},
            "Spc26": {"Name": "Samina", "Class": "7th", "Program": "Arts", "Condition": "Bad", "Scholarship": "Yes on 25%", "Marks": 39},
            "Spc27": {"Name": "Moiz", "Class": "7th", "Program": "Science", "Condition": "Normal", "Scholarship": "No", "Marks": 67}
        }
        self.Teachers = {
            "Tec23": {"Name": "Dark King", "Specific_skill": "Computer", "Salary": 54000, "Feedback": "Great", "Class_Teacher": "9th"},
            "Tec24": {"Name": "Sun God", "Specific_skill": "Math", "Salary": 67000, "Feedback": "Great", "Class_Teacher": "12th"},
            "Tec25": {"Name": "Red Hair", "Specific_skill": "Bio", "Salary": 78000, "Feedback": "Great", "Class_Teacher": "11th"},
            "Tec26": {"Name": "Beast King", "Specific_skill": "Arts", "Salary": 34000, "Feedback": "Good", "Class_Teacher": "11th"},
        }
        self.Admin = {
            "Adm23": {"Name": "Nami", "Role": "IT Specialist", "Salary": 50000, "Incharge": "Registration"},
            "Adm24": {"Name": "Robin", "Role": "Data Scientist", "Salary": 50000, "Incharge": "Data Management"},
            "Adm25": {"Name": "Sanji", "Role": "Finance Specialist", "Salary": 50000, "Incharge": "Finance"},
        }
        self.permissions = {
            "student": ["view_own_data"],
            "teacher": ["view_students", "modify_attendance"],
            "admin": ["add_user", "remove_user", "modify_data"]
        }
        self.programs = ["ICS", "ADP", "BSC", "B.Com", "I.Com", "B.Tech"]
        self.Scholarships = {
            "Beginner": {"percent": "50%", "Eligibility": "55%"},
            "IT": {"percent": "55%", "Eligibility": "60%"},
            "PM": {"percent": "89%", "Eligibility": "90%"},
            "CM-Punjab1": {"percent": "40%", "Eligibility": "55%"},
            "CM-Punjab2": {"percent": "75%", "Eligibility": "80%"},
            "Uni-1": {"percent": "50%", "Eligibility": "60%"}
        }

    def save(self):
        data = {
            "students": self.students,
            "teachers": self.Teachers,
            "admin": self.Admin,
            "permissions": self.permissions,
            "programs": self.programs,
            "Scholarships": self.Scholarships
        }
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4)
        print("💾 Database saved successfully!")


class Admin(DataBase):
    def add_student(self):
        try:
            ID = input("Enter new Student ID: ").strip()
            if ID in self.students:
                raise ValueError("⚠️ Student already exists!")

            Name = input("Enter student name: ").strip()
            print("Available programs:", self.programs)
            Program = input("Select Program: ").strip()
            Marks = int(input("Enter student marks (0–100): "))

            # Scholarship Eligibility
            scholarship = "No"
            if Marks >= 90:
                scholarship = "Eligible for PM"
            elif 80 <= Marks < 90:
                scholarship = "Eligible for CM-Punjab2"
            elif 70 <= Marks < 80:
                scholarship = "Eligible for Uni-1"
            elif 60 <= Marks < 70:
                scholarship = "Eligible for IT"
            elif 55 <= Marks < 60:
                scholarship = "Eligible for Beginner"
            else:
                scholarship = "Not Eligible"

            # Save student data
            self.students[ID] = {
                "Name": Name,
                "Program": Program,
                "Marks": Marks,
                "Scholarship": scholarship
            }

            print(f"✅ Student {Name} added successfully with scholarship status: {scholarship}")
            self.save()
        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"❌ Unexpected Error: {e}")

    def update_teacher_salary(self):
        try:
            ID = input("Enter Teacher ID: ").strip()
            if ID not in self.Teachers:
                raise KeyError("Teacher not found!")

            new_salary = int(input("Enter new salary: "))
            self.Teachers[ID]["Salary"] = new_salary
            print(f"✅ Salary updated for {self.Teachers[ID]['Name']} → {new_salary}")
            self.save()
        except Exception as e:
            print(f"❌ Error: {e}")


class Teacher(DataBase):
    def mark_attendance(self):
        try:
            student_id = input("Enter Student ID: ").strip()
            if student_id not in self.students:
                raise KeyError("Student not found!")
            status = input("Mark Attendance (Present/Absent): ").strip().capitalize()
            self.students[student_id].setdefault("Attendance", []).append(status)
            print(f"📘 Attendance marked for {student_id}: {status}")
            self.save()
        except Exception as e:
            print(f"❌ Error: {e}")


class Student(DataBase):
    def view_details(self):
        try:
            ID = input("Enter your student ID: ").strip()
            if ID not in self.students:
                raise KeyError("Student not found!")
            print(json.dumps(self.students[ID], indent=4))
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    print("\n🎓 --- School Management System --- 🎓")
    db = DataBase()

    while True:
        print("\n1️⃣ Admin Menu\n2️⃣ Teacher Menu\n3️⃣ Student Menu\n4️⃣ Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            ad = Admin()
            print("\n--- Admin Menu ---")
            print("1. Add Student\n2. Update Teacher Salary")
            sub = input("Choose: ")
            if sub == "1":
                ad.add_student()
            elif sub == "2":
                ad.update_teacher_salary()
            else:
                print("Invalid Option.")

        elif choice == "2":
            tec = Teacher()
            tec.mark_attendance()

        elif choice == "3":
            stu = Student()
            stu.view_details()

        elif choice == "4":
            print("👋 Exiting System. Goodbye!")
            break

        else:
            print("Invalid Input. Try Again.")