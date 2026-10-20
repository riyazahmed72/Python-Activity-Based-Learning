# CASE STUDY 8: Manufacturing Cost and Profitability Analysis

material = float(input("Material cost: Rs. "))
labor = float(input("Labor cost: Rs. "))
overhead = float(input("Overhead cost: Rs. "))
units = int(input("Units produced: "))

if material < 0 or labor < 0 or overhead < 0 or units <= 0:
    print("Invalid input.")
else:
    total_cost = material + labor + overhead
    cost_per_unit = total_cost / units
    profit = total_cost * 0.20
    total_revenue = total_cost + profit
    selling_price = total_revenue / units
    
    print("\n--- Manufacturing Summary ---")
    print("Total manufacturing cost: Rs.", round(total_cost, 2))
    print("Cost per unit: Rs.", round(cost_per_unit, 2))
    print("Target profit (20%): Rs.", round(profit, 2))
    print("Selling price per unit: Rs.", round(selling_price, 2))