def Tip_calculator(bill_amount ,tip_percentage,):
    calculated_tip = (bill_amount * tip_percentage) / 100
    print(f"Your total Bill is : {bill_amount} and tip amount is :{(bill_amount * tip_percentage) / 100}, Thank you ")
    return calculated_tip
Tip_calculator(2000, 15)
