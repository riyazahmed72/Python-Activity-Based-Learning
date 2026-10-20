# CASE STUDY 10: Campus Event Financial Planning

tickets = int(input("Tickets sold: "))
price = float(input("Price per ticket: Rs. "))
sponsorship = float(input("Total sponsorship amount: Rs. "))
expenses = float(input("Total event expenses: Rs. "))

if tickets < 0 or price < 0 or sponsorship < 0 or expenses < 0:
    print("Invalid input.")
else:
    revenue = (tickets * price) + sponsorship
    net = revenue - expenses
    
    print("\n--- Event Financial Statement ---")
    print("Total Revenue: Rs.", round(revenue, 2))
    print("Total Expenses: Rs.", round(expenses, 2))
    
    if net > 0:
        print("Net Profit: Rs.", round(net, 2))
    elif net < 0:
        print("Net Loss: Rs.", round(abs(net), 2))
    else:
        print("Break-even (No profit, no loss)")