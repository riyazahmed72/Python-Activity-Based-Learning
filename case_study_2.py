# Case Study 2: Progressive Electricity Billing

units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units.")
else:
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5
        
    if units > 200:
        fixed = 50
        surcharge = energy * 0.05
    else:
        fixed = 50
        surcharge = 0
        
    total = energy + fixed + surcharge
    
    print("\n--- Electricity Bill ---")
    print("Energy charge: Rs.", round(energy, 2))
    print("Fixed charge: Rs.", fixed)
    print("Surcharge: Rs.", round(surcharge, 2))
    print("Total bill: Rs.", round(total, 2))