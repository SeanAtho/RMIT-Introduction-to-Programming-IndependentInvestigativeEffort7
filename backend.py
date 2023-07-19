class Vehicles():
    make_model = None
    price = 0
    
class InventoryManager():
    inventory = []

    def add_car (self,invn_make_model,invn_price):
        inventory = Vehicles()
        inventory.make_model = invn_make_model
        inventory.price = invn_price
        self.inventory.append(inventory)

    def get_summary(self):
        summary = ""
        i = 0
        while (i <  len(inventory)):
            summary += inventory[i][0]+ "\t\t"
            summary += str(inventory[i][1])+ "\n"
            i+= 1
        return summary

    def load_inventory(self,inventory,filename):
        file_object = open(filename, "r")
        line = file_object.readline()
        
        line = file_object.readline()
        while (line != ""):
            fields = line.strip().split("\t\t")
            invn_make_model = fields[0]
            invn_price = float(fields[1])
            self.add_car(invn_make_model, invn_price)
            line = file_object.readline()
            
        file_object.close()

    def save_inventory(self,inventory,filename): 
        try:
            file_object = open(filename, "w")
            numb_cars = len(inventory)
            i = 0
            while (i < numb_cars):
                file_object.write("Make and Model\t\tPrice\n")
                file_object.write(inventory[i].make_model+ "\t\t" +str(inventory[i].price)+ "\n")
                i += 1
            file_object.close()
        except:
            sys.stdout.write("Could not save to file.")
