# ---------------------------------------------------------------
# Author: Krishna Mahajan
# course: Btech.cse 
# Subject: python programming 
# Purpose: Gradebook Analyzer
# ---------------------------------------------------------------

print("--------------------------------------------------")
print("           WELCOME TO GRADEBOOK ANALYZER")
print("--------------------------------------------------")

repeat = int(input("How many times do you want to run the analysis? "))

for run in range(repeat):

    print("\nRun:", run + 1)

    marks = {}   # store names + marks

    n = int(input("Enter number of students: "))

    # ----- INPUT -----
    for i in range(n):
        name = input(f"Enter student {i+1} name: ")
        score = float(input("Enter marks: "))
        marks[name] = score

    # ----- STATISTICS -----
    scores = sorted(marks.values())
    total = 0
    for s in scores:
        total += s
    average = total / len(scores)

    if len(scores) % 2 == 1:
        median = scores[len(scores)//2]
    else:
        median = (scores[len(scores)//2 - 1] + scores[len(scores)//2]) / 2

    # Highest & Lowest
    names = list(marks.keys())
    first = names[0]
    max_name = min_name = first
    max_score = min_score = marks[first]

    for name in marks:
        if marks[name] > max_score:
            max_score = marks[name]
            max_name = name
        if marks[name] < min_score:
            min_score = marks[name]
            min_name = name

    print("\n----- STATISTICS -----")
    print("Average:", average)
    print("Median :", median)
    print("Highest:", max_name, "->", max_score)
    print("Lowest :", min_name, "->", min_score)

    # ----- GRADES -----
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grades[name] = "A"
        elif score >= 80:
            grades[name] = "B"
        elif score >= 70:
            grades[name] = "C"
        elif score >= 60:
            grades[name] = "D"
        else:
            grades[name] = "F"

    # Grade counts
    A = B = C = D = F = 0
    for g in grades.values():
        if g == "A":
            A += 1
        elif g == "B":
            B += 1
        elif g == "C":
            C += 1
        elif g == "D":
            D += 1
        else:
            F += 1

    print("\n----- GRADE DISTRIBUTION -----")
    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("D:", D)
    print("F:", F)

    # ----- PASS / FAIL -----
    passed = []
    failed = []

    for name, score in marks.items():
        if score >= 40:
            passed.append(name)
        else:
            failed.append(name)

    print("\n----- PASS / FAIL SUMMARY -----")
    print("Passed:", passed)
    print("Failed:", failed)

    # ----- FINAL TABLE -----
    print("\n----- FINAL RESULT TABLE -----")
    print("Name\tMarks\tGrade")
    print("----------------------------")

    for name in marks:
        print(name, "\t", marks[name], "\t", grades[name])

print("\nProgram Finished. Thank you!")
