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

def coc_roi():
    #Introduction
    print("Allow me to calculate your rental property's Return on Investment (ROI). Only use numbers ( no $ or ,).")

    #Income
    print("First, let's calculate your Income.")
    ri = int(input("How much is your Rental Income? "))
    li = int(input("How much is your Laundry Income? "))
    si = int(input("How much is your Storage Income? "))
    mi = int(input("Please input the amount of any Miscellaneous Income. "))
    inc = ri + li + si + mi
    print(f'Your Total Monthly Income is ${inc}.')

    #Expenses
    print("Thank you.  Now, onto the Expenses for this rental property.")
    tax = int(input("How much do you pay in Taxes? "))
    ins = int(input("How much do you pay in Insurance? "))
    ele = int(input("How much do you pay for Electricity? "))
    h2o = int(input("How much do you pay for Water? "))
    sew = int(input("How much do you pay for Sewage? "))
    gas = int(input("How much do you pay for Gas? "))
    utl = ele + h2o + sew + gas
    hoa = int(input("How much do you pay in HOA fees? "))
    ls =  int(input("How much do you pay for lawn/yard/snow cleanup? "))
    vac = int(input("How much do you want to set aside for Vacancy? "))
    rep = int(input("How much do you want to put aside for Repairs? "))
    capex = int(input("How much do you want to put aside for those big projects? (aka Capital Expenses) "))
    pm = int(input("How much are you spending on Property Management? "))
    mort = int(input("How much is your Mortgage? "))
    exp = tax + ins+ utl + hoa + ls + vac + rep + capex + pm + mort
    print(f'Your Total Montly Expenses is ${exp}')

    #Cash Flow
    print("Thanks again.  Now that we have that information, we can calculate your Cash Flow.")
    tmcf = inc - exp
    print("No worries!  I've got this one!")
    print(f"Your Total Montly Cash Flow is ${tmcf}")

    #ROI
    print("Just a few more questions and I will have your ROI.")
    acf = tmcf * 12
    dp = int(input("How much did you put on the Down Payment? "))
    cc = int(input("How much were the Closing Costs? "))
    rb = int(input("How much was your Rehab Budget? (money to fix property) "))
    mo = int(input("Please input any Miscellaneous costs. "))
    ti = dp + cc + rb + mo
    roi = (acf/ti) * 100
    print("And now... the moment you've been waiting for!!!")
    print(f"Your Cash on Cash Return on Investment for this rental property is {roi}%! (Don't @ me!)")

coc_roi()


#   roi = (acf/ti) * 100
#   acf = tmcf * 12
#   ti = dp + cc + rb + mo
#   tmcf = inc - exp
#   inc = ri + li + si + mi
#   exp = tax + ins+ utl + hoa + ls + vac + rep + capex + pm + mort
#   utl = ele + h2o + sew + gas