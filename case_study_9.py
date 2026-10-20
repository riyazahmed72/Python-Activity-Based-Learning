# CASE STUDY 9: Multi-Currency Travel Budget Analysis

inr_budget = float(input("Enter budget in INR: "))
print("Choose currency: 1. USD, 2. EUR, 3. GBP")
choice = int(input("Enter choice (1-3): "))
expense = float(input("Estimated trip expense in foreign currency: "))

if inr_budget < 0 or expense < 0 or choice < 1 or choice > 3:
    print("Invalid input.")
else:
    if choice == 1:
        converted = inr_budget / 83
        c_name = "USD"
    elif choice == 2:
        converted = inr_budget / 90
        c_name = "EUR"
    else:
        converted = inr_budget / 105
        c_name = "GBP"
        
    print("\n--- Travel Budget Summary ---")
    print("Converted Budget:", round(converted, 2), c_name)
    
    if expense <= converted:
        print("Status: Within budget")
    else:
        print("Status: Budget exceeded")