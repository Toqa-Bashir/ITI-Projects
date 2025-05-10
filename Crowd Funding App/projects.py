class Projects:
    users = [] 
    project_title = ""
    don = 0
    project_target = ""
    @classmethod
    def donate (cls):
        name = input( " Please enter the project name : ")
        with open ("projects.txt" ,"r") as file : 
            users = file.readlines()
            project_found = False
            for index in range(len(users)) :
                user = users[index].strip()
                data2= user.split(":")  
                if len(data2) == 5 :
                    project_title, project_details, project_category, project_target, project_time = data2
                
                    if name == project_title:  
                        print(f"Project found:\nTitle: {project_title}\nDetails: {project_details}\nCategory: {project_category}\nTarget: {project_target}\nTime: {project_time}")

                        don = input("Please enter the amount of donation: ")
                        print(f"Thank you for donating {don} to the project '{project_title}'")
                        new_don = f" Donations : {don} "
                        users[index]=user.strip() + new_don +"\n"
                        project_found = True
                        break
            if project_found :
                with open("projects.txt" , "w") as file :
                    file.writelines(users)

    @classmethod                   
    def delete (cls) :
                    global don
                    with open ("projects.txt" ,"r") as file : 
                        users = file.readlines()
                        pr_name = input( " Enter the project name ")
                        pr_found = False
                        for index in range(len(users)) :
                            user = users[index].strip()
                            data2= user.split(":")  
                            if len(data2) == 5 :
                                project_title, project_details, project_category, project_target, project_time = data2
                            
                                if pr_name == project_title and float (don) < (0.25*float(project_target)):
                                    del users[index]
                                    pr_found = True
                                    break
                        if pr_found :
                                    with open("projects.txt" , "w") as file :
                                            file.writelines(users)
                                    print(f"The project '{pr_name}' has been deleted.")
                        else :
                            print( " Sorry, donations exceed 25% of the target . You can't delete that project!")
                            
    @classmethod
    def create (cls):
        title = input(" Enter project title : ")
        details = input(" Please clarify th project details : ")
        category = input("Please clarify the category : ")
        target = (input(" Please specify the total target : "))
        time = input("Please set the start date and end date for the project : ")
        data = f"{title}:{details}:{category}:{target}:{time}\n"
        with open ("projects.txt","a") as file :
            file.write(data + "\n")
        ans = input(" Would you like to participate by donating to a project ? ")
        if ans == "yes" :  
             pr_1.donate()  
        ans2 = input(" Do you want to delete a project ? (yes/no)")
        if ans2 =="yes" :
            pr_1.delete()

pr_1=Projects()