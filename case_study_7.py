# CASE STUDY 7: Retail Billing with Multiple Discount Rules

p1 = float(input("Item 1 price: "))
q1 = int(input("Item 1 quantity: "))
p2 = float(input("Item 2 price: "))
q2 = int(input("Item 2 quantity: "))
p3 = float(input("Item 3 price: "))
q3 = int(input("Item 3 quantity: "))
is_member = input("Premium member? (yes/no): ").lower()

if p1 < 0 or q1 < 0 or p2 < 0 or q2 < 0 or p3 < 0 or q3 < 0:
    print("Invalid input.")
else:
    subtotal = (p1 * q1) + (p2 * q2) + (p3 * q3)
    discount = 0
    
    if subtotal >= 5000:
        discount += subtotal * 0.05
    if is_member == "yes":
        discount += subtotal * 0.10
        
    net_amount = subtotal - discount
    
    print("\n--- Retail Bill Summary ---")
    print("Subtotal: Rs.", round(subtotal, 2))
    print("Total discount: Rs.", round(discount, 2))
    print("Net payable: Rs.", round(net_amount, 2))