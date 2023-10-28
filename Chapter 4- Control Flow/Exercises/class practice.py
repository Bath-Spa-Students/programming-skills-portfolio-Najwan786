#control structure
#decision structure

sales= float(input("Enter sales :"))
bonus= 0
if sales > 50000 :
    bonus = 500
else:
    bonus = 0
    print("Your bonus: "+str(bonus))

marks = float(input("enter marks :"))
if marks > 30:
    marks = "PASS"
else:
    marks = "FAIL"
print("your marks: "+str(marks))
