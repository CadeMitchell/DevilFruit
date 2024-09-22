from src.fruit_manager import *
from src.utilities import *

def main():
    #File Select
    choice = menu_generator([("New Save File", "New"), ("Load Save File", "Load")])
    if choice == "Load":
        file = load_file()
    else:
        name = input("Please input save name: ")
        file = {"name": name, "fruits": []}
        save_file(file)
        
        
    #Menu
    manager = Fruit_Manager(file)
    choices = [("Exit and Save", "Exit"), ("Pick Fruit", "Pick"), ("View Fruit", "View"), ("Add Fruit", "Add"), ("Edit Fruit", "Edit"), ("Delete Fruit", "Delete")]
    while True:
        choice = menu_generator(choices)
        clear()
        
        if choice == "Exit":
            file = manager.export()
            save_file(file)
            break
        
        elif choice == "Pick":
            manager.raffle_fruit()
                    
        elif choice == "View":
            manager.view_fruit()
                
        elif choice == "Add":
            manager.add_fruit()
                
        elif choice == "Edit":
            manager.edit_fruit()    
        
        elif choice == "Delete":
            manager.remove_fruit()
            


if __name__ == "__main__":
    clear()
    main()