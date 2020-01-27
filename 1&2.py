#LAB ACTIVITY 1
IDNumber = input("Input your 8 digit ID Number")
IDNumber1 = int((IDNumber[0])) * int (8)
IDNumber2 = int((IDNumber[1])) * int (7)
IDNumber3 = int((IDNumber[2])) * int (6)
IDNumber4 = int((IDNumber[3])) * int (5)
IDNumber5 = int((IDNumber[4])) * int (4)
IDNumber6 = int((IDNumber[5])) * int (3)
IDNumber7 = int((IDNumber[6])) * int (2)
IDNumber8 = int((IDNumber[7])) * int (1)
ALL =  int (IDNumber1)+int(IDNumber2)+int(IDNumber3)+int(IDNumber4)+int(IDNumber5)+int(IDNumber6)+int(IDNumber7)+int(IDNumber8)
if (ALL % 11 ==0):
        if (ALL  %  11 < 16):
            print("Student")  
        elif (ALL  %  11 > 16):
            print("faculty")
else:
        print("The ID is Fake")

