class User :    

    password =""

    def __init__(self):
        pass
    
    @classmethod
    def mobile_validation (cls):
        import re
        pattern = r"^01[0-2]\d{8}$"
        valid = False
        while True :
            global mobile 
            mobile = input("Enter your moblie phone : ") 
            if re.match(pattern , mobile) :
                return mobile
            else:
                print(" Egyptian moblie numbers only . Please try again")
               
    @classmethod
    def Registration (cls):
        fname = input("Enter your first name : ")
        lname = input("Enter your last name : ")
        Email = input("Enter your email : " )
        password = input("Enter your password : ") 
        mobile=cls.mobile_validation()
        valid = False
        
        while True :
            c_password = input("confirm your password : ") 
            if password == c_password : 
                data = f" {fname}:{lname}:{Email}:{password}:{mobile}\n"
                print(data)
                valid = True
                
            else :
                print (" passwords don't match , please cofirm the password")
            with open("users.txt","a") as file :
                file.write(data)
                return data
    @classmethod
    def update(cls,users,index):
                old = int(input(" Please choose what to change : 1 first name , 2 last name , 3 password , 4 mobile "))
                if old not in [1,2,3,4] :
                    print(" Invalid choice ")
                    return 
                user = users[index].strip()
                data = user.split(":")
                fname, lname, Email, password, mobile = data    
                new = input( " Enter the new data : ")
                if old == 1 :
                    fname = new
                elif old == 2 :
                        lname = new
                elif old == 3 :
                        password = new
                elif old == 4 :
                        mobile = new
                users[index] = f"{fname}:{lname}:{Email}:{password}:{mobile}\n"   
                with open("users.txt" ,"w") as file :
                        file.writelines(users) 
                print(" Profile updated succesfuly ")    
                print("Updated record:")
                print(users[index])
                return users    
    @classmethod
    def add(cls,users,index):            
                choice = input(" Please choose what to add : Birthdate ,  Facebook URL , country : ")
                new = input( " Enter the new data : ")
                new_data =f"{choice}:{new} \n" 
                print(new_data)
                
                user = users[index].strip()
                data = user.split(":")
                users[index] = users[index].strip() + ":" + new_data + "\n"

                with open("users.txt" , "a") as file :
                    file.writelines(users)
                with open("users.txt" , "w") as file :
                    file.writelines(users)
                print(" Profile updated succesfuly ")    
                print("Updated record:")
                print(users[index])
    @classmethod
    def delete (cls,users,index):             
                confirm = input(" Your data will be deleted forever! Are you sure ? ")
                if confirm == "yes":
                    pas = input(" Please enter your password ") 
                    user = users[index].strip()
                    data = user.split(":")
                    fname, lname, Email, password, mobile = data
                    if pas == password:
                        del users[index]
                        with open("users.txt" ,"w") as file :
                            file.writelines(users) 
                        print(" Your accound has been deleted ")
                        return users
                else:
                    print("Deletion cancelled")
                    return users     
                        
    @classmethod
    def view(cls):   
                try :                  
                    with open ("projects.txt","r") as file :
                        projects = file.readlines()
                    for project in projects :
                        print(project)
                    
                except FileNotFoundError :
                     print("Error! No projects found ")   
                              
    @classmethod
    def login (cls):
        while True : 
                e = input("Enter your email : ")
                p =input("Enter your password : ")
                found = False
                with open ("users.txt" , "r") as file :
                    users = file.readlines()
                for index in range(len(users)) :
                    user = users[index].strip()
                    data = user.split(":")
            
                    if len(data) == 5:
                        fname, lname, Email, password, mobile = data
                        if e == Email and p == password :
                            print (f" Hello {fname} {lname}")
                            with open("users.txt","r") as file :
                                print(user)
                            found = True 
                            break
                if found : 
                    break        
            
                retry = input("Not found . Do you want to try again ? ")
                if retry != "yes" : 
                    print("Thank you . Goodbye!")
                    break

            
        if found :
            ans = input(" Do you want to update your profile ? (yes / no ) ")
            if ans == "yes" :
                user_1.update(users,index)
            else:
                print("No changes made ")    


            ans = input(" Do you want to add to your profile ? (yes / no ) ")
            if ans == "yes" : 
                 user_1.add(users,index)
            else : 
                print("No changes made")

            des = input(" Do you want to delete your account ? (yes / no )")
            if des == "yes" :
                 user_1.delete(users,index)
            else : 
                print("No changes made")

            view =input(" Do you want to view your projects ? ")
            if view == "yes" :
                user_1.view()
    @classmethod
    def logout(cls):
            out = input("Do you want to log out ?(yes/no)")
            if out == "yes" :
                 print(" Thank you for choosing TOGETHER app :)")
                 exit()    
               
user_1 = User()
