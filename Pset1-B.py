def hunting_house_b(total_cost, portion_saved, annual_salary, semi_annual_raise):

    portion_down_payment = 0.25 * total_cost
    current_savings = 0
    r = 0.04
    months = 0

    while (current_savings <= portion_down_payment):

        monthly_salary = annual_salary / 12

        current_savings = current_savings + (current_savings * r / 12) + (portion_saved * monthly_salary)
        
        months += 1

        if (months % 6) == 0:
            annual_salary = annual_salary + (annual_salary * semi_annual_raise)
        
    print("No.of.months ", months)

hunting_house_b(500000, .05, 120000, .03)
