# CASE STUDY 4: Employee Payroll and Deduction Analysis

basic = float(input("Basic pay (Rs.): "))
hours = float(input("Overtime hours: "))
incentive = float(input("Incentive (Rs.): "))

if basic < 0 or hours < 0 or incentive < 0:
    print("Invalid input.")
else:
    hra = basic * 0.20
    other = basic * 0.10
    overtime = hours * 150
    gross = basic + hra + other + overtime + incentive
    deduction = gross * 0.08
    net = gross - deduction
    
    print("\n--- Salary Statement ---")
    print("Basic pay: Rs.", round(basic, 2))
    print("HRA: Rs.", round(hra, 2))
    print("Other allowance: Rs.", round(other, 2))
    print("Overtime pay: Rs.", round(overtime, 2))
    print("Incentive: Rs.", round(incentive, 2))
    print("Gross salary: Rs.", round(gross, 2))
    print("Deduction: Rs.", round(deduction, 2))
    print("Net salary: Rs.", round(net, 2))