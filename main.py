#Using VS Code, Jupytor Notebook, and Object Oriented Programming, create a program that will calculate the Return on Investment(ROI) for a rental property.

#1. Income
#   Duplex
#       Rental Income = $2K
#       Laundry Income = 0
#       Storage Income= 0
#       Misc Income= 0
#   TOTAL MONTHLY INCOME = $2K

#2. Expenses
#       Tax = $150
#       Insurance = $100
#       Utilities = 0
#           Electric = 0
#           Water = 0
#           Sewer = 0
#           Gas = 0
#       HOA = 0
#       Lawn/Snow = 0
#       Vacancy = $100
#       Repairs = $100
#       Captial Expdenditures (CapEx) = $100
#       Property Management = $200
#       Mortgage: = $860
#   TOTAL MONTHLY EXPENSES = $1,610

#3. Cash Flow
#       Income - Expenses
#       2000    -   1610
#           $390
#   TOTAL MONTHLY CASH FLOW = $390

#4. Cash on Cash ROI
#       Down Payment = $40K
#       Closing Costs = $3K
#       Rehab Budget = $7K
#       Misc Other = 0
#   TOTAL INVESTMENT = $50K

#       Total Montly Cash Flow * 12
#               390     *   12
#       Annual Cash flow = $4,680
#       Annual Cash flow / Total Investment
#           4680 / 50000
#               .0963 = 9.36%
#   CASH ON CASH ROI = 9.36%

# *****FIRST DRAFT *****

# def coc_roi():
#     #Introduction
#     print("Allow me to calculate your rental property's Return on Investment (ROI). Only use numbers ( no '$' or ',').")

#     #Income
#     print("First, let's calculate your Income.")
#     ri = int(input("How much is your Rental Income? "))
#     li = int(input("How much is your Laundry Income? "))
#     si = int(input("How much is your Storage Income? "))
#     mi = int(input("Please input the amount of any Miscellaneous Income. "))
#     inc = ri + li + si + mi
#     print(f'Your Total Monthly Income is ${inc}.')

#     #Expenses
#     print("Thank you.  Now, onto the Expenses for this rental property.")
#     tax = int(input("How much do you pay in Taxes? "))
#     ins = int(input("How much do you pay in Insurance? "))
#     ele = int(input("How much do you pay for Electricity? "))
#     h2o = int(input("How much do you pay for Water? "))
#     sew = int(input("How much do you pay for Sewage? "))
#     gas = int(input("How much do you pay for Gas? "))
#     utl = ele + h2o + sew + gas
#     hoa = int(input("How much do you pay in HOA fees? "))
#     ls =  int(input("How much do you pay for lawn/yard/snow cleanup? "))
#     vac = int(input("How much do you want to set aside for Vacancy? "))
#     rep = int(input("How much do you want to put aside for Repairs? "))
#     capex = int(input("How much do you want to put aside for those big projects? (aka Capital Expenses) "))
#     pm = int(input("How much are you spending on Property Management? "))
#     mort = int(input("How much is your Mortgage? "))
#     exp = tax + ins+ utl + hoa + ls + vac + rep + capex + pm + mort
#     print(f'Your Total Montly Expenses is ${exp}')

#     #Cash Flow
#     print("Thanks again.  Now that we have that information, we can calculate your Cash Flow.")
#     tmcf = inc - exp
#     print("No worries!  I've got this one!")
#     print(f"Your Total Montly Cash Flow is ${tmcf}")

#     #ROI
#     print("Just a few more questions and I will have your ROI.")
#     acf = tmcf * 12
#     dp = int(input("How much did you put on the Down Payment? "))
#     cc = int(input("How much were the Closing Costs? "))
#     rb = int(input("How much was your Rehab Budget? (money to fix property) "))
#     mo = int(input("Please input any Miscellaneous costs. "))
#     ti = dp + cc + rb + mo
#     roi = (acf/ti) * 100
#     print("And now... the moment you've been waiting for!!!")
#     print(f"Your Cash on Cash Return on Investment for this rental property is {roi}%! (Don't @ me!)")

# coc_roi()

# *****END OF FIRST DRAFT*****

#       MATH
#   roi = (acf/ti) * 100
#   acf = tmcf * 12
#   ti = dp + cc + rb + mo
#   tmcf = inc - exp
#   inc = ri + li + si + mi
#   exp = tax + ins+ utl + hoa + ls + vac + rep + capex + pm + mort
#   utl = ele + h2o + sew + gas



class ROI():
    def __init__(self):
        self.addIncome = 0
        self.addExpenses = 0

    def incomeCalc(self):
        print("Let's calculate your Income from this rental property.")
        rental_income = int(input("How much is your Rental Income? "))
        laundry_income = int(input("How much is your Laundry Income? "))
        storage_income = int(input("How much is your Storage Income? "))
        misc_income = int(input("Please input the amount of any Miscellaneous Income. "))
        income = rental_income + laundry_income + storage_income + misc_income
        print(f'Your Total Monthly Income is ${income}.')
        self.addIncome = income

    def expensesCalc(self):
        print("Let's calculate your Expenses for this rental property.")
        taxes = int(input("How much do you pay in Taxes? "))
        insurance = int(input("How much do you pay in Insurance? "))
        electricity = int(input("How much do you pay for Electricity? "))
        water = int(input("How much do you pay for Water? "))
        sewage = int(input("How much do you pay for Sewage? "))
        gasex = int(input("How much do you pay for Gas? "))
        utilities = electricity + water + sewage + gasex
        homeowners = int(input("How much do you pay in HOA fees? "))
        lawn_yard_snow =  int(input("How much do you pay for lawn/yard/snow cleanup? "))
        vacancy = int(input("How much do you want to set aside for Vacancy? "))
        repairs = int(input("How much do you want to put aside for Repairs? "))
        capitalex = int(input("How much do you want to put aside for those big projects? (aka Capital Expenses) "))
        propman = int(input("How much are you spending on Property Management? "))
        mortgage = int(input("How much is your mortgage? "))
        expenses = taxes + insurance+ utilities + homeowners + lawn_yard_snow + vacancy + repairs + capitalex + propman + mortgage
        print(f'Your Total Montly Expenses is ${expenses}')
        self.addExpenses = expenses

    def onlyROI(self):
        print("Let's calculate your Return on Investment (ROI).")
        roiincome = int(input("How much Income are you making from this property? "))
        roiexpenses = int(input("How much are your Expenses for this propery? "))
        cashflow = roiincome - roiexpenses
        print(f"Your Total Montly Cash Flow is ${cashflow}")
        annual_cashflow = cashflow * 12
        down_payment = int(input("How much did you put on the Down Payment? "))
        closing_costs = int(input("How much were the Closing Costs? "))
        rehab_budget = int(input("How much was your Rehab Budget? (money to fix property) "))
        misc_costs = int(input("Please input any Miscellaneous costs. "))
        total_investment = down_payment + closing_costs + rehab_budget + misc_costs
        roi_coc = (annual_cashflow/total_investment) * 100
        print("And now... the moment you've been waiting for!!!")
        print(f"Your Cash on Cash Return on Investment for this rental property is {roi_coc}%.")

    def completeROI(self):
        print("Thank you.  Now that we have that information, we can calculate your Cash Flow.")
        cashflow = self.addIncome - self.addExpenses
        print("No worries!  I've got this one!")
        print(f"Your Total Montly Cash Flow is ${cashflow}")
        print("Just a few more questions and I will have your ROI.")
        annual_cashflow = cashflow * 12
        down_payment = int(input("How much did you put on the Down Payment? "))
        closing_costs = int(input("How much were the Closing Costs? "))
        rehab_budget = int(input("How much was your Rehab Budget? (money to fix property) "))
        misc_costs = int(input("Please input any Miscellaneous costs. "))
        total_investment = down_payment + closing_costs + rehab_budget + misc_costs
        roi_coc = (annual_cashflow/total_investment) * 100
        print("And now... the moment you've been waiting for!!!")
        print(f"Your Cash on Cash Return on Investment for this rental property is {roi_coc}%.")

    def runner(self):
        while True:
            choice = input('Would you like to calculate you "Income", "Expenses", "ROI", or "All"? (type income, expenses, roi, all, or quit)').lower()
            if (choice == 'quit'):
                break
            elif (choice == 'income'):
                self.incomeCalc()
            elif (choice == 'expenses'):
                self.expensesCalc()
            elif (choice == 'roi'):
                self.onlyROI()
            elif (choice == 'all'):
                self.incomeCalc()
                self.expensesCalc()
                self.completeROI()
            else:
                print('Invalid input, please try again...')

ROI = ROI()
ROI.runner()