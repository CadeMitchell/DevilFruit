from src.fruit_manager import *
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
        save_file(file)
        
        
    #Menu
    choices = [("Exit and Save", "Exit"), ("Pick Fruit", "Pick"), ("View Fruit", "View"), ("Add Fruit", "Add"), ("Edit Fruit", "Edit"), ("Delete Fruit", "Delete")]
    while True:
        choice = menu_generator(choices)
        clear()
        
        if choice == "Exit":
            save_file(file)
            break
        
        elif choice == "Pick":
            pass
                    
        elif choice == "View":
            pass
                
        elif choice == "Add":
            pass
                
        elif choice == "Edit":
            pass    
        
        elif choice == "Delete":
            pass
            


if __name__ == "__main__":
    clear()
    main()