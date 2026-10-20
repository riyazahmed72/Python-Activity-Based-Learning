# CASE STUDY 6: Railway Fare and Reservation Calculator

distance = float(input("Distance (km): "))
print("Classes: 1. Sleeper, 2. AC 3-Tier, 3. AC First Class")
travel_class = int(input("Enter class choice (1-3): "))
age = int(input("Passenger age: "))

if distance < 0 or age < 0 or travel_class < 1 or travel_class > 3:
    print("Invalid input.")
else:
    if travel_class == 1:
        rate = 1.50
    elif travel_class == 2:
        rate = 2.50
    else:
        rate = 4.00
        
    base_fare = distance * rate
    
    if age < 5:
        final_fare = 0
    elif age >= 60:
        final_fare = base_fare * 0.75
    else:
        final_fare = base_fare
        
    print("\n--- Railway Ticket Summary ---")
    print("Base fare: Rs.", round(base_fare, 2))
    print("Final ticket fare: Rs.", round(final_fare, 2))