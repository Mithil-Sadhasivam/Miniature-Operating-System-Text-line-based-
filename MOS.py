import os
import sys

notepad = 0
my_files = 0
calc = 0
sksks = 0

def run(to):
    print(f"\n--- Running {to} ---")

print("MOS 1.5 | Type 'help' for more details")
print("Module OK")

while True:
    if notepad == 0 and my_files == 0:
        command = input("\nCommand? ").strip().lower()
    else:
        command = ""

    if command == "notepad":
        notepad = 1
        run("Notepad")

    while notepad == 1:
        print("\n[NOTEPAD] 1.Create  2.Write  3.Read  4.Exit")
        choice = input("Choice? ")
        
        if choice == "1":
            file_name = input("New File Name? ")
            try:
                f = open(file_name, "x")
                f.close()
                print("File created.")
            except FileExistsError:
                print("Error: File already exists.")
                
        elif choice == "2":
            file_name = input("File Name to write to? ")
            text = input("Text? ")
            try:
                f = open(file_name, "a")
                f.write(text + "\n")
                f.close()
                print("Text appended.")
            except FileNotFoundError:
                print("Error: File not found.")
            
        elif choice == "3":
            file_name = input("File Name to read? ")
            try:
                f = open(file_name, "r")
                print("\n--- FILE CONTENT ---")
                print(f.read())
                print("--------------------")
                f.close()
            except FileNotFoundError:
                print("Error: File not found.")
                
        elif choice == "4":
            notepad = 0

    if command == "progman":
        my_files = 1
        run("Progman")
    
    while my_files == 1:
        print("\n[PROGMAN] 1.Directory_List  2.Delete  3.Open  4.Exit")
        file_choice = input("Choice? ")
        
        if file_choice == "1":
            print("\nDirectory in Drive A:")
            files = os.listdir('.') 
            for file in files:
                print(f" > {file}")

        elif file_choice == "2":
            file_del = input("File Name to delete? ")
            file_del = file_del.strip().lower()
            if (file_del == "mos.py"):
                print("Access Denied!File required for Operating System")
            else:
                try:
                    os.remove(file_del)
                    print(f"{file_del} deleted successfully.")
                except FileNotFoundError:
                    print("Error: File not found.")
                except PermissionError:
                    print("Error: Permission denied.")

        elif file_choice == "3":
            file_open = input("File to open? ")
            try:
                f = open(file_open, "r")
                print("\n--- FILE CONTENT ---")
                print(f.read())
                print("--------------------")
                f.close()
            except FileNotFoundError:
                print("Error: File not found.")
        
        elif file_choice == "4":
            my_files = 0
            
    if command == "exit":
        sys.exit("Operating system shutdown")

    if command == "help":
        print("Available commands: notepad, progman, calc, run, dir")
            
    if command == "calc":
        calc = 1
        run("Calculator")
    while (calc == 1):
        print("\n[CALC] 1.Calculate  2.Exit")
        calc_choice = input("Choice? ")
        
        if calc_choice == "1":
            x = float(input("First no?"))
            y = float(input("Second no?"))
            operator = input("Operator?(a,s,m,d,?)")
            if operator =="a":
                print(x + y)
            elif operator =="s":
                print(x - y)
            elif operator == "m":
                print(x * y)
            else:
                print(x / y)     
        elif calc_choice == "2":
            calc = 0
    if command == "run":
        file_to_run = input("File to run (e.g. app.py)? ")
        if os.path.exists(file_to_run):
            run(file_to_run)
            try:
                with open(file_to_run, "r") as f:
                    exec(f.read()) 
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("File not found on Disk A.")

    valid_commands = ["notepad", "progman", "calc", "run", "help", "exit", "name a legend", "dir"]

    if command not in valid_commands and command != "":
        print("Bad command or file name")
        
    if (command == "name a legend"):
        print("Technoblade, without a doubt, man.")
    
    if (command == "dir"):
        print("\nDirectory in Drive A:")
        files = os.listdir('.') 
        for file in files:
            print(f" > {file}")
        
        

    
            

    

