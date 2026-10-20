# CASE STUDY 5: Multi-Plan Telecommunications Cost Optimization

usage = float(input("Monthly data usage (GB): "))
budget = float(input("Monthly budget (Rs.): "))

if usage < 0 or budget < 0:
    print("Invalid input.")
else:
    cost_a = 199 + max(0, usage - 2) * 50
    cost_b = 299 + max(0, usage - 5) * 30
    cost_c = 399 + max(0, usage - 10) * 20
    
    plans = [("Plan A", cost_a), ("Plan B", cost_b), ("Plan C", cost_c)]
    
    print("Plan A cost: Rs.", round(cost_a, 2))
    print("Plan B cost: Rs.", round(cost_b, 2))
    print("Plan C cost: Rs.", round(cost_c, 2))
    
    best_name = ""
    best_cost = 0
    
    for name, cost in plans:
        if cost <= budget and (best_name == "" or cost < best_cost):
            best_name = name
            best_cost = cost
            
    if best_name == "":
        print("No plan is within your budget.")
    else:
        print("Recommended plan:", best_name)
        print("Monthly cost: Rs.", round(best_cost, 2))