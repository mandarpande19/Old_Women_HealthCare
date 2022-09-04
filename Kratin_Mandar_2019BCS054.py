import pandas as pd
import csv
from tabulate import tabulate


def old_women(age):
    
# This systeam is useful if you have 65+ age if it is not 65 or more than that then your are not eligible for use this systeam
    if age>=65:

        # The age is 65+ hence you should proceed further Enter the Your weight

        # Their are 3 types of conditions that are the normal weight , Under weight , Over weight 

        weight=int(input("Enter your weight:-"))
        
        # If your weight is normal menas in between 50 to 75 then followed futher condintion if not then the systeam check next condition
        # In that the old women get the schedule for her whole week
        if 50<=weight<=75:
            print("Your weight is normal...")
            print("Please follows the below schedule for your Healthy and Better life...")

            with open('normal.csv') as normal_csv:
                    normal_csv_reader = csv.reader(normal_csv)
                    normal_rows = list(normal_csv_reader)
            print(tabulate(normal_rows,headers='firstrow',tablefmt='grid'))

        # If the old women want only a perticular day schedule then type yes

            yes_no=str(input("If you want to get only one particular Day schedule (yes / no) ::- "))


            if yes_no == "yes":
                normal = pd.read_csv("normal.csv")
                normal_row_no= int(input(" Enter number(for monday 1, and so on upto sun is 7) ::- "))
                print(normal.loc[[0,normal_row_no]])


            else :
                print("Thanks a lot !!! For supporting us ")

        # If you are under weight means weight is less than 50 then followed futher condintion if not then the systeam check next condition
        # In that the old women get the schedule for her whole week


        elif weight<50:
            print("You are under weight...")
            print("Please follows the below schedule for weight gain and your Healthy , Better life...")
            

            with open('under.csv') as under_csv:
                    under_csv_reader = csv.reader(under_csv)
                    under_rows = list(under_csv_reader)
            print(tabulate(under_rows,headers='firstrow',tablefmt='grid'))
            
            
        # If the old women want only a perticular day schedule then type yes

            yes_no = str(input("If you want to get only one particular Day schedule (yes / no) ::-  "))
            
            if yes_no == "yes":
                under = pd.read_csv("under.csv")
                under_row_no= int(input(" Enter number(for monday 1, and so on upto sun is 7) ::- "))
                print(under.loc[[0,under_row_no]])


            else:
                print("Thanks a lot !!! For supporting us ")

        # If you are over weight menas more than 75 then followed futher condintion if not then the systeam check next condition
        # In that the old women get the schedule for her whole week


        elif weight>75:
            print("You are over weight...")
            print("Please follows the below schedule for weight loss64 and your Healthy , Better life...")

            """normal = pd.read_csv("over.csv")
            print(normal)"""

            with open('over.csv') as over_csv:
                    over_csv_reader = csv.reader(over_csv)
                    over_rows = list(over_csv_reader)
            print(tabulate(over_rows,headers='firstrow',tablefmt='grid'))

        # If the old women want only a perticular day schedule then type yes

            yes_no = str(input("If you want to get only one particular Day schedule (yes / no) ::- "))

            if yes_no == "yes":
                over = pd.read_csv("over.csv")
                over_row_no= int(input(" Enter number(for monday 1, and so on upto sun is 7) ::- "))
                
                print(over.loc[[0,over_row_no]])


            else:
                print("Thanks a lot !!! For supporting us ")

    else :
        print("you are not eligible for the treatment...","\n This systeam is useful only for 65+ old people\n")
        print("THANK YOU FOR VISITING OUR SYSTEAM...")


print("HELLO MADAM/SIR..","\nWE ARE FROM KRATIN HEALTHCARE CENTER FROM NAGPUR\n")
print("WE ARE HELPING THE OLD AGE PEOPLE","\nFOR THEIR HEALTHY HAPPY LIFE AND BETTER LIFE\n")



age=int(input("Enter your age:-"))
old_women(age)

