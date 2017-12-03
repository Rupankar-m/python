def day(x):  
    day_server = (0.51 * x)
    return day_server

def month(x):
    month_server = (0.51 * x)
    return month_server

def budget(x):
    budget_server = (x / 0.51)
    return budget_server

def pound(y):
    print ("Do you want to convert your pence into pounds?")
    pound_function = (y / 100)
    print ("You have: £" , pound_function)
    

def menu():
    print ("""Welcome to my Cloud Hosting program. It will compute how much it will cost to operate servers
       Type 1 to work out the cost of hosting 1 server for a day
       Type 2 to work out cost of hosting 1 server for a month
       Type 3 to work out the cost of hosting your desired servers for a day
       Type 4 to work out the cost of hosting your desired servers for a month
       Type 5 to work out how many servers you can host while on a budget
       Type 0 to exit the application""")
    
#======================================================================================================

while True:
    menu()
    user_input = int(input("Please enter your option: "))    

    if user_input == 1:
        x = 24
        day_server = day(x)
        print ("It will cost you: " , day_server , "p")
        y = day_server
        pound(y)

    
    if user_input == 2:
        x = 24 * 30
        month_server = month(x)
        print ("It will cost you: " , month_server , "p")
        y = month_server
        pound(y)
       

    if user_input == 3:
        days_hosted = int(input("Please type how many servers you want to host in a day: "))
        x = 24 * days_hosted
        day_server = day(x)
        print ("It will cost you: " , day_server , "p")
        y = day_server
        pound(y)
        

    if user_input == 4:
        months_hosted = int(input("Please type how many servers you want to host in a month: "))
        x = 24 * 30 * months_hosted
        month_server = month(x)
        print ("It will cost you: " , month_server , "p")
        y = month_server
        pound(y)

    if user_input == 5:
        budget_hosted = float(input("Please type your budget in pence"))
        x = budget_hosted
        budget_server = budget(x)
        print ("You can host: " , budget_server , " servers")
        
        
    if user_input == 0:
        print ("Thank You!!")
        break


     


