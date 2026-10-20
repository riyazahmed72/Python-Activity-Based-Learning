# Case Study 1: University Scholarship Allocation

name = input("Applicant name: ")
m1 = float(input("Subject 1 marks: "))
m2 = float(input("Subject 2 marks: "))
m3 = float(input("Subject 3 marks: "))
attendance = float(input("Attendance percentage: "))
income = float(input("Family annual income (Rs.): "))

if (m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100 or attendance < 0 or attendance > 100 or income < 0):
    print("Invalid input.")
else:
    percentage = (m1 + m2 + m3) / 3
    print("Applicant:", name)
    print("Aggregate percentage:", round(percentage, 2))
    
    if m1 >= 50 and m2 >= 50 and m3 >= 50 and attendance >= 75 and income <= 300000:
        print("Result: Eligible for scholarship")
    else:
        print("Result: Not eligible for scholarship")