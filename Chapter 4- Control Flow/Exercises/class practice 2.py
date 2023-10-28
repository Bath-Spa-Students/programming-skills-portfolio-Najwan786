#nested desicion structure
earning = int(input("ENTER YOUR EARNING PER YEAR:"))
work_experience = float (input("ENTER YOUR WORK EXPERIENCE:"))

if earning > 30000:
    if work_experience >=2:
        print("YOUR ARE ELIGIBLE FOR LOAN")
    else :
        print("Sorry, Your work experience is less than 2 years ")
else:
    print("Your earning is less than 30000")

#Example
earning = int(input)("ENTER YOUR EARNING PER YEAR: ")

