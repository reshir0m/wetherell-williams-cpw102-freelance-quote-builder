def main():
    nameRaw = input("Client name: ")
    hours = input("Estimated work hours: ")
    rate = input("Hourly rate: ")
    expenses = input("Direct expenses: ")
    laborCost = CalculateLaborCost(rate, hours)
    totalCost = CalculateTotal(laborCost, expenses)
    print("\nPROJECT ESTIMATE")
    FormatName(nameRaw)
    FormatCost("Labor cost:", laborCost)
    FormatCost("Direct expenses:", expenses)
    FormatCost("Total estimate:", totalCost)

def CalculateLaborCost(rate, hours):
    laborCost = float(rate) * float(hours)
    return laborCost

def CalculateTotal(labor, directExpenses):
    total = float(labor) + float(directExpenses)
    return total

def FormatName(name):
    name = name.strip().title()
    print("Client: " + name)

def FormatCost(lineText, dollars):
    amount = round(float(dollars), 2)
    print(lineText + " $" + str(amount))

main()
