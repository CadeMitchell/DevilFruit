from src.fruit import *
from src.utilities import *
import random
import pprint as pp

def import_json_file(file_name: str):
    pass

def export_json_file(fruit_dictionary: dict):
    pass




def main():
    #File Select
    choice = menu_generator([("New Save File", "New"), ("Load Save File", "Load")])
    if choice == "Load":
        file = load_file()
    else:
        name = input("Please input save name.")
        file = {"name": name, "fruit": []}
    
    #Menu
    while True:
        choices = [("Exit and Save", "Exit"), ("Pick Fruit", "Pick"), ("View Fruit", "View"), ("Add Fruit", "Add"), ("Edit Fruit", "Edit"), ("Delete Fruit", "Delete")]
        
        if choice == "Exit":
            save_file(file)
            break
        elif choice == "Pick":
            if len(file["fruit"]) > 0:
                zipped_raffle = [(fruit["name"], fruit["weight"]) for fruit in file if fruit["avaiable"]]
                fruit_raffle = [name[0] for name in zipped_raffle]
                weight_raffle = [weight[1] for weight in zipped_raffle]
                winner = random.choices(fruit_raffle, weight_raffle)
                
                print(f"Winning Fruit: {winner}")
                user = input("Would you like to take this unavaiable for future rolls?\n(Y)es\n(N)o").upper()
                if user == "Y":
                    find = [fruit for fruit in file if fruit["name"] == winner]
                    index = file["fruit"].index(find)
                    file["fruit"][index]["avaiable"] = False
        elif choice == "View":
            if len(file["fruit"]) > 0:
                all_fruit = [(fruit["name"], fruit) for fruit in file]
                choice = menu_generator(all_fruit)
                pp.pprint(choice)
        elif choice == "Add":
            pass
        elif choice == "Edit":
            pass
        elif choice == "Delete":
            pass
                    
    
    #Do selected action
    
    


if __name__ == "__main__":
    main()