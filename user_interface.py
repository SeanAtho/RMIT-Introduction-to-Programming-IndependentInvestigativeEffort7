import sys
import backend

def get_str(prompt):
    sys.stdout.write(prompt)
    entered_str = sys.stdin.readline().strip()
    while (entered_str == ""):
        sys.stdout.write("Error! Enter a valid input. \n")
        entered_str = sys.stdin.readline().strip()
        
    return entered_str

def main_interface():
    inventory = backend.InventoryManager()
    #The string variable is created and used to store the main interface and
    #menu which indicates the available options to the user.
    #Prevents unnecessary use of stdouts and prints in code blocks. 
    menu = ""
    menu += "===============\n"
    menu += "Car Dealerships\n"
    menu += "===============\n"
    menu += "[L]oad inventory\n"
    menu += "[A]dd vehicle\n"
    menu += "[D]isplay cars\n"
    menu += "E[x]it\n"
    menu += "[S]ave inventory \n"
    menu += "Choice: \n"
    
    sys.stdout.write(menu)
    choice = sys.stdin.readline().strip().lower()
    while (choice != "x"):
        sys.stdout.write("\n")
        #If is created to allow for the user to display car inventory file
        if (choice == "l"):
            sys.stdout.write("Load Inventory...\n")
            filename = get_str("Enter filename: ")
            backend.InventoryManager()

        #Elif used for the user's input enables make, model and price of choice to
        #be stored in variable make_model.   
        elif (choice == "a"):
            make_model = get_str("Enter make and model: \n")

            input_ok = False
            #While loop created for checking of price data type.
            while (input_ok == False):
                price_str = get_string("Enter price: \n")
                #Try except constructed for invalid inputs with the appropriate message
                #displayed to the user indicating incorrect input.
                try:
                    price = float(price_str)
                    input_ok = True
                except:
                    sys.stdout.write("Invalid price input! \n")

            backend.InventoryManager()
        #Elif used to display all cars contained within the inventory,
        #organized with an interface specifying each section.  
        elif (choice == "d"):
            sys.stdout.write("Displaying cars...\n")
            summary = backend.InventoryManager()
            sys.stdout.write("Make and model\t\tPrice\n")
            sys.stdout.write(str(summary))
        #Elif to save inventory to file in the programs folder
        elif (choice == "s"):
            sys.stdout.write("Saving Cars... \n")
            filename = get_string("Enter file name: \n")
            backend.InventoryManager()
        #Else used to handle an invalid input from the user following the choice at the main menu. 
        else:
            sys.stdout.write("Invalid choice! \n")

        sys.stdout.write(menu)
        choice = sys.stdin.readline().strip().lower()
    sys.stdout.write("Program finished. \n")
main_interface()
