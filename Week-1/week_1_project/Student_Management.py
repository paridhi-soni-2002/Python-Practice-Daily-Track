students = []

while True:

    print("\n====================================")
    print("   STUDENT RESULT MANAGEMENT")
    print("====================================")
    print("1. Add Student")
    print("2. View Results")
    print("3. View Statistics")
    print("4. Search Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter Choice: ")

    # ADD STUDENT
    if choice == "1":

        name = input("\nEnter Student Name: ")

        marks = []

        for i in range(1, 6):

            while True:

                mark = int(input(f"Enter Subject {i} Marks: "))

                if mark < 0 or mark > 100:
                    print("Invalid Marks! Enter between 0 and 100.")
                    continue

                marks.append(mark)
                break

        attendance = float(input("Enter Attendance %: "))

        total = sum(marks)
        average = total / 5
        percentage = total / 5

        highest = max(marks)
        lowest = min(marks)

        failed_subjects = 0

        for mark in marks:
            if mark < 35:
                failed_subjects += 1

        # Result Status
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

        # Performance
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

    # VIEW RESULTS
    elif choice == "2":

        if len(students) == 0:
            print("No Student Records Found!")
            continue

        name = input("Enter Student Name: ")

        found = False

        for student in students:

            if student["name"].lower() == name.lower():

                found = True

                print("\n========================================")
                print("             RESULT CARD")
                print("========================================")

                print("Student Name      :", student["name"])

                print("\nMarks:")

                for i in range(5):
                    print(f"Subject {i+1}         : {student['marks'][i]}")

                print("\nTotal Marks       :", student["total"])
                print("Average Marks     :", student["average"])
                print("Percentage        :", student["percentage"], "%")

                print("\nHighest Mark      :", student["highest"])
                print("Lowest Mark       :", student["lowest"])

                print("\nAttendance        :", student["attendance"], "%")
                print("Eligibility       :", student["eligibility"])

                print("Failed Subjects   :", student["failed_subjects"])

                print("\nGrade             :", student["grade"])
                print("Result Status     :", student["result"])

                print("Performance       :", student["performance"])

                print("========================================")

        if not found:
            print("Student Not Found!")

    # VIEW STATISTICS
    elif choice == "3":

        if len(students) == 0:
            print("No Student Records Found!")
            continue

        total_students = len(students)

        passed = 0
        failed = 0

        topper_name = ""
        topper_percentage = 0

        class_total = 0

        for student in students:

            class_total += student["percentage"]

            if student["result"] == "PASS":
                passed += 1
            else:
                failed += 1

            if student["percentage"] > topper_percentage:
                topper_percentage = student["percentage"]
                topper_name = student["name"]

        class_average = class_total / total_students

        print("\n====================================")
        print("            STATISTICS")
        print("====================================")

        print("Total Students       :", total_students)
        print("Passed Students      :", passed)
        print("Failed Students      :", failed)

        print("\nClass Average        :", round(class_average, 2), "%")

        print("\nTopper Student       :", topper_name)
        print("Topper Percentage    :", topper_percentage, "%")

        print("====================================")

    # SEARCH STUDENT
    elif choice == "4":

        search_name = input("Enter Student Name: ")

        found = False

        for student in students:

            if student["name"].lower() == search_name.lower():

                found = True

                print("\nStudent Found!")
                print("Name :", student["name"])
                print("Percentage :", student["percentage"])
                print("Result :", student["result"])

        if not found:
            print("Student Not Found!")

    # DISPLAY ALL STUDENTS
    elif choice == "5":

        if len(students) == 0:
            print("No Student Records Found!")
            continue

        print("\n========== ALL STUDENTS ==========")

        for student in students:

            print("\nName :", student["name"])
            print("Percentage :", student["percentage"])
            print("Grade :", student["grade"])
            print("Result :", student["result"])

    # EXIT
    elif choice == "6":

        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")