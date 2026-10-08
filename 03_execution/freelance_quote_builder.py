def project_estimate(name,hours, rate, d_expenses,):
    
    # Processing the calculations from user inputs
    client_name = name
    labor_cost = hours * rate
    dir_exp = (d_expenses)
    tot_est = (labor_cost + dir_exp)

    return client_name, labor_cost, dir_exp, tot_est


def main():

    # User Inputs
    name = input("Client name: ").strip().title()
    hours = float(input("Estimated work hours: "))
    rate = float(input("Hourly rate: "))
    d_expenses = float(input("Direct expenses: "))


    # Calls the return statement from project_estimate
    client_name, labor_cost, dir_exp, tot_est = project_estimate(name, hours, rate, d_expenses,)


    # Output calculations from user inputs
    print("\n")
    print("PROJECT ESTIMATE")
    print("Client name:", (client_name))
    print(f"Labor cost: ${labor_cost:.2f}")
    print(f"Direct cost: ${dir_exp:.2f}")
    print(f"Total estimate: ${tot_est:.2f}")

main()