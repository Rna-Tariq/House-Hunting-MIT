def house_hunting(total_cost, portion_saved, annual_salary):

    portion_down_payment = 0.25 * total_cost
    current_savings = 0
    r = 0.04
    annual_return = (current_savings * r) / 12
    monthly_salary = annual_salary / 12
    portion_saved = portion_saved * monthly_salary 
    months = 0

    while (current_savings <= portion_down_payment):
        months += 1
        current_savings += (current_savings * r / 12) + portion_saved  
    print("No.of.months ", months)

house_hunting(1000000, .10, 120000)
