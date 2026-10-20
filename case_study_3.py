# CASE STUDY 3: Hospital Billing and Patient Classification

age = int(input("Patient age: "))
consult = float(input("Consultation charge: Rs. "))
diagnostic = float(input("Diagnostic charge: Rs. "))
treatment = float(input("Treatment charge: Rs. "))

if age < 0 or consult < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid input.")
else:
    subtotal = consult + diagnostic + treatment
    if age >= 60:
        discount = subtotal * 0.10
    else:
        discount = 0
        
    final_bill = subtotal - discount
    
    if final_bill < 1000:
        category = "Basic"
    elif final_bill < 5000:
        category = "Standard"
    else:
        category = "High"
        
    print("\n--- Hospital Bill ---")
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Concession: Rs.", round(discount, 2))
    print("Final bill: Rs.", round(final_bill, 2))
    print("Bill category:", category)