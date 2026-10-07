def main():
    nameRaw = AskName()
    hours = AskHours()
    rate = AskRate()
    expenses = AskExpenses()
    laborCost = CalculateLaborCost(rate, hours)
    totalCost = CalculateTotal(laborCost, expenses)
    print("PROJECT ESTIMATE")
    FormatName(nameRaw)
    FormatCost("Labor cost:", laborCost)
    FormatCost("Direct expenses:", expenses)
    FormatCost("Total estimate:", totalCost)


def AskName():
    nameRaw = input("Client name: ")
    return nameRaw

def AskHours():
    hours = input("Estimated work hours: ")
    return hours

def AskRate():
    rate = input("Hourly rate: ")
    return rate

def AskExpenses():
    expenses = input("Direct expenses: ")
    return expenses

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
