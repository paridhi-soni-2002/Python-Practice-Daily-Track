# STUDENT RESULT MANAGEMENT SYSTEM


students = []
subjects = ["English", "Hindi", "Maths", "Science", "Social"]

while True:

    print("\n====================================")
    print("    STUDENT RESULT MANAGEMENT")
    print("====================================")
    print("1. Add Student")
    print("2. View Result")
    print("3. View Statistics")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter Choice: ")

    # ADD STUDENT
  
    if choice == "1":

        name = input("\nEnter Student Name: ")

        marks = []

        for subject in subjects:

            while True:

                mark = int(input(f"Enter {subject} Marks: "))

                if mark < 0 or mark > 100:
                    print("Invalid Marks! Enter marks between 0 and 100.")
                    continue

                marks.append(mark)
                break

        attendance = float(input("Enter Attendance Percentage: "))

        # Calculations
        total = sum(marks)
        average = total / len(marks)
        percentage = (total / 500) * 100

        highest = max(marks)
        lowest = min(marks)

        # Count failed subjects
        failed_subjects = 0

        for mark in marks:
            if mark < 35:
                failed_subjects += 1

        # Result
        if failed_subjects == 0:
            result = "PASS"
        else:
            result = "FAIL"

        # Eligibility
        if attendance >= 75:
            eligibility = "Eligible"
        else:
            eligibility = "Not Eligible"

        # Grade
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        else:
            grade = "Fail"

        # Performance Category
        if percentage >= 90:
            performance = "Excellent"
        elif percentage >= 80:
            performance = "Very Good"
        elif percentage >= 70:
            performance = "Good"
        elif percentage >= 60:
            performance = "Average"
        else:
            performance = "Needs Improvement"

        student = {
            "name": name,
            "marks": marks,
            "attendance": attendance,
            "total": total,
            "average": average,
            "percentage": percentage,
            "highest": highest,
            "lowest": lowest,
            "failed_subjects": failed_subjects,
            "eligibility": eligibility,
            "grade": grade,
            "result": result,
            "performance": performance
        }

        students.append(student)

        print("\nStudent Added Successfully!")

    # VIEW RESULT
    elif choice == "2":

        if len(students) == 0:
            print("No Student Records Found!")
            continue

        search_name = input("Enter Student Name: ")

        found = False

        for student in students:

            if student["name"].lower() == search_name.lower():

                found = True

                print("\n========================================")
                print("              RESULT CARD")
                print("========================================")

                print("Student Name      :", student["name"])

                print("\nSubject Wise Marks")

                for subject, mark in zip(subjects, student["marks"]):
                    print(subject, ":", mark)

                print("\nTotal Marks       :", student["total"])
                print("Average Marks     :", round(student["average"], 2))
                print("Percentage        :", round(student["percentage"], 2), "%")

                print("\nHighest Mark      :", student["highest"])
                print("Lowest Mark       :", student["lowest"])

                print("\nAttendance        :", student["attendance"], "%")
                print("Eligibility       :", student["eligibility"])

                print("\nSubject Status")

                # zip() usage again
                for subject, mark in zip(subjects, student["marks"]):

                    if mark >= 35:
                        status = "PASS"
                    else:
                        status = "FAIL"

                    print(f"{subject}: {status}")

                print("\nFailed Subjects   :", student["failed_subjects"])

                print("Grade             :", student["grade"])
                print("Result Status     :", student["result"])
                print("Performance       :", student["performance"])

                print("========================================")
                break

        if not found:
            print("Student Not Found!")

    # VIEW STATISTICS
    
    elif choice == "3":

        if len(students) == 0:
            print("No Student Records Found!")
            continue

        total_students = len(students)

        passed_students = 0
        failed_students = 0

        topper_name = ""
        topper_percentage = 0

        total_percentage = 0

        for student in students:

            total_percentage += student["percentage"]

            if student["result"] == "PASS":
                passed_students += 1
            else:
                failed_students += 1

            if student["percentage"] > topper_percentage:
                topper_percentage = student["percentage"]
                topper_name = student["name"]

        class_average = total_percentage / total_students

        print("\n====================================")
        print("            STATISTICS")
        print("====================================")

        print("Total Students      :", total_students)
        print("Passed Students     :", passed_students)
        print("Failed Students     :", failed_students)

        print("\nClass Average       :", round(class_average, 2), "%")

        print("\nTopper Student      :", topper_name)
        print("Topper Percentage   :", round(topper_percentage, 2), "%")

        print("====================================")

    # SEARCH STUDENT
    
    elif choice == "4":

        if len(students) == 0:
            print("No Student Records Found!")
            continue

        search_name = input("Enter Student Name: ")

        found = False

        for student in students:

            if student["name"].lower() == search_name.lower():

                found = True

                print("\nStudent Found!")
                print("Name       :", student["name"])
                print("Percentage :", round(student["percentage"], 2), "%")
                print("Grade      :", student["grade"])
                print("Result     :", student["result"])

                break

        if not found:
            print("Student Not Found!")

    # DISPLAY ALL STUDENTS

    elif choice == "5":

        if len(students) == 0:
            print("No Student Records Found!")
            continue

        print("\n====================================")
        print("           ALL STUDENTS")
        print("====================================")

        for index, student in enumerate(students, start=1):

            print(f"\nStudent {index}")
            print("Name       :", student["name"])
            print("Percentage :", round(student["percentage"], 2), "%")
            print("Grade      :", student["grade"])
            print("Result     :", student["result"])

    # EXIT
    elif choice == "6":

        print("Exiting Program...")
        break

    else:
        print("Invalid Choice! Please Try Again.")