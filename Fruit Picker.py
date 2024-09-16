from src.fruit import *
from src.utilities import *
import random

def main():
    #File Select
    choice = menu_generator([("New Save File", "New"), ("Load Save File", "Load")])
    if choice == "Load":
        file = load_file()
    else:
        name = input("Please input save name.")
        file = {"name": name, "fruit": []}
        
        
    #Menu
    choices = [("Exit and Save", "Exit"), ("Pick Fruit", "Pick"), ("View Fruit", "View"), ("Add Fruit", "Add"), ("Edit Fruit", "Edit"), ("Delete Fruit", "Delete")]
    while True:
        choice = menu_generator(choices)
        clear()
        
        if choice == "Exit":
            save_file(file)
            break
        
        elif choice == "Pick":
            if len(file["fruit"]) < 1:
                input("No fruit to choose from...")
                continue
            zipped_raffle = [(fruit, fruit["weight"]) for fruit in file["fruit"] if fruit["available"] == True]
            if not zipped_raffle:
                input("No fruit in available. Make fruit available and try again...\n")
                continue
            fruit_raffle = [fruit[0] for fruit in zipped_raffle]
            weight_raffle = [weight[1] for weight in zipped_raffle]
            winner = random.choices(fruit_raffle, weight_raffle)[0]
            
            print(f"Winning Fruit: {winner["fruit_name"]}")
            user = input("Would you like to remove the fruit from future rolls?\n(Y)es\n(N)o\nInput: ").upper()
            if user == "Y":
                index = file["fruit"].index(winner)
                file["fruit"][index]["available"] = False
                    
        elif choice == "View":
            if len(file["fruit"]) > 0:
                all_fruit = [(fruit["fruit_name"], fruit) for fruit in file["fruit"]]
                choice = menu_generator(all_fruit)
                clear()
                fruit_obj = Fruit(choice["fruit_name"], choice["type"], choice["weight"], choice["fruit_desc"], choice["abilities"] ,choice["available"])
                print(fruit_obj)
                input("Continue\n")
                
        elif choice == "Add":
            fruit_name = input("Fruit Name: ")
            fruit_type =  input("Fruit Type: ")
            fruit_desc = input("Input short fruit description:\n")
            fruit_weight = input("Input the weight chance of the fruit (Think Raffle Tickets): ")
            fruit_available = menu_generator([("Yes", True), ("No", False)], "Do you want this fruit avaiable in the raffle right now?")
            abilities = []
            while True:
                add_choice = menu_generator([("Done", "Exit"), ("Add Ability", "Add")], "Add an ability?\n(Can be added later)")
                if add_choice == "Exit":
                    break
                ability_name = input("Ability Name: ")
                ability_desc = input("Ability Description:\n")
                abilities.append({"ability_name": ability_name, "ability_desc": ability_desc})
                
            new_fruit = Fruit(fruit_name, fruit_type, fruit_desc, fruit_weight, abilities, fruit_available)
            file["fruit"].append(new_fruit.export())
                
            
        elif choice == "Edit":
            pass
        elif choice == "Delete":
            pass


if __name__ == "__main__":
    clear()
    main()