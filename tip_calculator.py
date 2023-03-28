food_amount = input("Enter the amount of food you want to order :" )
tip_Percentage = input("Enter the Tip percentage :  ")     # 20% = 20/100
tip_amount = int(food_amount) *float(tip_Percentage)

# total = tip_amount + food_amount
Total = float(tip_amount) + float(food_amount)

#printing the final Receipt 
print("------------------------------------")
print("Ordered Food amount  : " + str(food_amount))
print("Tip Amount : " + str(tip_amount))
print("------------------------------------")
print('Rs ' + str(Total)) # here combining the String and decimal
print("------------------------------------")
'''
str(100) --> will be read as a string 
'''


# ABOVE same program using function
def billing(Food_amt,Tip_percent):
    print("Enter Food Amount  :" )
    print("\n")
    print("Enter Tip Percent  :" )
    print("\n")
    tip_amt = float(Food_amt) * float(Tip_percent)
    Total = float(tip_amt) + float(Food_amt)
    
    print("------------------------------------")
    print("------------------------------------")
    print("Ordered Food amount  : " + str(Food_amt))
    print(f'Tip amount : {tip_amt}')    
    print("------------------------------------")
    print('Rs ' + str(Total)) 
    print("------------------------------------")

billing(500,0.20)
