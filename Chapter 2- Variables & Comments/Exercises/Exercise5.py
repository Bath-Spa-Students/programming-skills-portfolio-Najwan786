# A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each. Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left. You will to use the arithmetic operators to complete this exercise.suppose girl's money = a and price for usbsticks = b
a = int(input("INPUT HOW MUCH MONEY THE GIRL HAS: "))
b = int(input("INPUT THE PRICE OF THE USB STICKS: "))

print("ABLE TO BUY=",a//b)
print("REMAINING AMOUNT=",a%b)
