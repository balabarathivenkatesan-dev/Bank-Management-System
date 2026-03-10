emp={}

def add_employee(emp_id,name,dept,salary):
    emp[emp_id]={"Name":name,
                 "Department":dept,
                 "Salary":salary}
    print(f"Employee {emp[emp_id]["Name"]} added  Successfully")

def view_employee():
    if emp:
        for id,details in emp.items():
            print(f"Emp_ID :{id} , Details : {details}")
    else:
        print("No Employees added Yet")
        
def update_employee(emp_id,name=None,dept=None,salary=None):
    try:
        if emp_id in emp.keys():
            if name:
                emp[emp_id]["Name"]=name
            if dept:
                emp[emp_id]["Department"]=dept
            if salary:
                emp[emp_id]["Salary"]=salary
        else:
            print("Employee does not exists")
    except KeyError:
        print(f"{e} exception occured")
    else:
        print("Updated Successfully")

def remove_employee(emp_id):
    del emp[emp_id]
    print("Employee removed successfully")

def save_to_file(filename):
    try:
        with open(filename,"w") as f:
            for id,details in emp.items():
                line=f"Emp_ID: {id} , Details: {details}"
                f.write(line)
    except:
        print(f"Error : {e}")
    else:
        print("Saved to file successfully") 
        
def load_from_file(filename):
    
    global emp
    emp={}
    try:
        with open(filename) as f:
            for  x in f:
                id,name,department,salary=x.strip().split(',')
                emp[id]={"Name":name,
                        "Department":department,
                        "Salary":salary}
    except FileNotFoundError:
        print(f"Error : File Not Found Error")
    except e:
        print(f"Error occured {e}")
    else:
        print("Loaded from file successfully")
    
            
def menu():
    while True:
        print("\nEmployee Management System...\n")
        print("1.Add Employee")
        print("2.View Employee")
        print("3.Update Employee")
        print("4.Remove Employee")
        print("5.Save to File")
        print("6.Load from File")
        print("7.Exit")
        print("-------------------------------\n")
        
        k=int(input("Enter your choice:"))
        
        if k==1:
            emp_id=input("Enter employee ID:")
            name=input("Enter employee name:")
            dept=input("Enter employee Department:")
            salary=input("Enter salary:")
            add_employee(emp_id,name,dept,salary)
        elif k==2:
            view_employee()
        elif k==3:
            emp_id=input("Enter employee ID for uppdate")
            name=input("Enter name if you wanna change else just click enter:")or None
            dept=input("Enter dept if you wanna change else just click enter:")or None
            salary=input("Enter salary if you wanna change else just click enter:")or None
            update_employee(emp_id,name,dept,salary)
        elif k==4:
            emp_id=input("Enter employee ID to remove")
            remove_employee(emp_id)
        elif k==5:
            filename=input("Enter filename:")
            save_to_file(filename)
        elif k==6:
            filename=input("Enter filename to load:")
            load_from_file(filename)
        elif  k==7:
            print("Existing System")
            break
        else:
            print("Entered Invalid Choice")
            
menu()