print("Welcome to TOGETHER Crowdfunding app :)")
while True:
        try:
            choice =int(input('Please choose from menu : 1 Regitration , 2 Login , 3 new Project , 4 donate, 5 logout '))
            if choice == 1 :
                from users_3 import User 
                User.Registration()
            elif choice == 2 :
                from users_3 import User
                User.login()     
            elif choice == 3 :
                from projects import Projects
                Projects.create()
            elif choice == 4 :
                from projects import Projects
                Projects.donate()
            elif choice == 5 :
                 from users_3 import User  
                 User.logout()   
                 break
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")

            retry=input(" Do you need another process ?(yes/no)")
            if retry!="yes" :
                 print(" Thank you for choosing TOGETHER app :)")
                 exit()
        except ValueError:
            print("Error! Please enter numbers only ")            
