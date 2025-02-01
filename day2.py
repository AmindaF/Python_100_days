print("welcome to the pay calculator")

total = float(input("what is the total bill? : $"));
people = int(input("how many people splitting the bill? "));
tip = int(input("the tip precentage you like to give (10,12,15)?"));
actual_tip = int((total/100) * tip);
bill = (total + actual_tip)/people;
round(bill, 2)


print(f"each person should pay ${bill}")