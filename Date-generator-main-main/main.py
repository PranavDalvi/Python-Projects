# hey there programmer this is basic date generator fork it and update it if you want. 
# If I liked your update I will copy paste your code in my repository with a your name on the code
pre_date = None

def user_input():
    print("\nNOTE: If you want to find date till 5 then enter 6 in ending date.")
    try:
        # start input from user
        date = int(input("\nPlease Enter Starting Date: "))
        month = int(input("\nPlease Enter Starting Month: "))
        year = int(input("\nPlease Enter Starting Year: "))

        # end input from user
        end_date = int(input("\nPlease Enter Ending Date: "))
        end_month = int(input("\nPlease Enter Ending Month: "))
        # end_year = int(input("Please Enter Ending Year: "))
        LeapYear(year)
    except:
        print("\nERROR: Unable to read try again\n")
        user_input()

    if date > 31 or month > 12 or year > 2100: # here Pylance gives warnings but it is totally ok
        print("\nERROR: Are you kidding me!? Try again\n")
        user_input()
    else:
        pre_date_list(date, month, year, end_date, end_month, pre_date)# here Pylance gives warnings but it is totally ok
    


def LeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def pre_date_list(date, month, year, end_date, end_month, pre_date):
    if month == 1: # January 
        pre_date = 32
    elif month == 2: # February and so on
        if LeapYear(year) == True:
            pre_date = 30
        else:
            pre_date = 29
    elif month == 3:
        pre_date = 32
    elif month == 4:
        pre_date = 31
    elif month == 5:
        pre_date = 32
    elif month == 6:
        pre_date = 31
    elif month == 7:
        pre_date = 32
    elif month == 8:
        pre_date = 32
    elif month == 9:
        pre_date = 31
    elif month == 10:
        pre_date = 32
    elif month == 11:
        pre_date = 31
    elif month == 12:
        pre_date = 32

    if end_month < month or end_date < date:
        print("\nERROR: Starting month or date is greater than ending month or date. Try again.\n")
        user_input()
    elif month != end_month: # if Month is not equal to End Month run this
        month_not_equal_end_month(date, month, year, end_date, end_month, pre_date)
    elif month == end_month: # if Month is equal to End Month run this
        month_equal_end_month(date, month, year, end_date, pre_date)
        

# if Month is equal to End Month function
def month_equal_end_month(date, month, year, end_date, pre_date):
    if end_date < pre_date:
        while date <= end_date:
            print(date, "/", month, "/", year)
            date += 1
            if date == end_date:
                inp = input("\nDone! Do you want to try again? Y = yes / Any key = no: ").upper()
                if inp == "Y":
                    user_input()
                else:
                    break

    elif end_date > pre_date:
        while date <= pre_date:
            print(date, "/", month, "/", year)
            date += 1
            inp = input("\nDone! Do you want to try again? Y = yes / Any key = no: ").upper()
            if inp == "Y":
                user_input()
            else:
                break


# if Month is not equal to End Month function
def month_not_equal_end_month(date, month, year, end_date, end_month, pre_date):
    
    while date < pre_date:
        
        print(date, "/", month, "/", year)
        date += 1
        if date == pre_date:
            increment_month(date, month, year, end_date, end_month, pre_date)


# here month will increment by 1 and date will be resetted to 1
def increment_month(date, month, year, end_date, end_month, pre_date): 
    date = 1
    month += 1
    print("") # this will leave space between previous amd next months
    pre_date_list(date, month, year, end_date, end_month, pre_date)

user_input()
