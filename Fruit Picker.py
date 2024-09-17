from src.fruit import *
from src.utilities import *
import random

def main():
    #File Select
    choice = menu_generator([("New Save File", "New"), ("Load Save File", "Load")])
    if choice == "Load":
        file = load_file()
    else:
        name = input("Please input save name: ")
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
            while True:
                option = [("Exit Menu", "Exit")]
                option.extend([(fruit["fruit_name"], fruit) for fruit in file["fruit"]])
                edit_fruit_choice = menu_generator(option, "Select which fruit you would like to edit, or 'Exit Menu' to retrun to main screen.")
                         
                if edit_fruit_choice == "Exit":
                    break
                
                fruit_obj = Fruit(edit_fruit_choice["fruit_name"], edit_fruit_choice["type"], edit_fruit_choice["weight"], 
                                    edit_fruit_choice["fruit_desc"], edit_fruit_choice["abilities"] ,edit_fruit_choice["available"])
                while True:
                    edit_option = [("Exit Menu", "Exit"), ("Edit Fruit Name", "Name"), ("Edit Fruit Type", "Type"), 
                                    ("Edit Fruit Description", "Desc"), ("Edit Fruit Weight", "Weight"), ("Toggle Fruit Availability", "Available"), 
                                    ("Add Fruit Ability", "Add"), ("Remove Fruit Ability", "Remove")]
                    edit_choice = menu_generator(edit_option, fruit_obj)
                    if edit_choice == "Exit":
                        index = file["fruit"].index(edit_fruit_choice)
                        file["fruit"][index] = fruit_obj.export()
                        break
                    elif edit_choice == "Name":
                        fruit_obj.edit_name(input("Enter New Name: "))
                    elif edit_choice == "Type":
                        fruit_obj.edit_fruit_type(input("Enter New Fruit Type: "))
                    elif edit_choice == "Desc":
                        fruit_obj.edit_desc(input("Enter New Fruit Description:\n"))
                    elif edit_choice == "Weight":
                        fruit_obj.edit_weight(input("Enter New Weight Chance: "))
                    elif edit_choice == "Available":
                        fruit_obj.toggle_avaiable()
                    elif edit_choice == "Add":
                        ability_name = input("Please type new ability name: ")
                        ability_desc = input("Please type new ability description:\n")
                        fruit_obj.add_ability(ability_name, ability_desc)
                    elif edit_choice == "Remove":
                        abilities_options = [("Cancel", "Exit")]
                        abilities_options.extend([(fruit_ability.name, fruit_ability) for fruit_ability in fruit_obj.abilities])
                        ability_remove_choice = menu_generator(abilities_options, "Select which fruit you would like to edit, or 'Cancel' to retrun to previous menu.")
                        if ability_remove_choice != "Exit":
                            fruit_obj.del_ability(ability_remove_choice)    
        
        elif choice == "Delete":
            while True:
                option = []
                option.append(("Exit Menu", "Exit"))
                option.extend([(fruit["fruit_name"], fruit) for fruit in file["fruit"]])
                del_choice = menu_generator(option, "Select which fruit you would like to delete, or 'Exit Menu' to retrun to main screen.")       
                if del_choice == "Exit":
                    break          
                index = file["fruit"].index(del_choice)
                file["fruit"].pop(index)
            


if __name__ == "__main__":
    clear()
    main()