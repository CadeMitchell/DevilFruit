from .fruit import Fruit, Ability
from .utilities import *
import random

class Fruit_Manager:
    def __init__(self, file: dict) -> None:
        self.file_name = file["name"]
        self.fruits = []
        if file["fruits"]:
            for fruit in file["fruits"]:
                self.fruits.append(Fruit(fruit))
            
    def add_fruit(self):
        fruit_dict = {}
        fruit_dict["fruit_name"] = input_validator("default", "Please input the Fruit's Name: ")
        fruit_dict["fruit_desc"] = input_validator("default", "Please input the Fruit's Description: ")
        fruit_dict["type"] = input_validator("default", "Please input the Fruit's Type: ")
        fruit_dict["weight"] = input_validator("number", "Please input the Fruit's raffle Weight: ")
        fruit_dict["available"] = menu_generator([("Yes", True), ("No", False)], "Do you want the Fruit immediatly avaiable in raffles?")
        fruit_dict["abilities"] = []
        while True:
            user = menu_generator([("Yes", True), ("No", False)], "Would you like to add an ability?")
            if not user:
                break
            ability = {}
            ability["ability_name"] = input_validator("default", "Please input the Ability's Name: ")
            ability["ability_desc"] = input_validator("default", "Please input the Ability's Description: ")
            fruit_dict["abilities"].append(ability)
            input("Ability Added. Press ENTER to continue.")
        new_fruit = Fruit(fruit_dict)
        user = menu_generator([("Yes", True), ("No", False)], "Keep and add this new fruit?\n" + str(new_fruit))
        if user:
            self.fruits.append(new_fruit)
            
    def remove_fruit(self):
        while True:
            default_options = [("Exit Remove Fruit Menu", "Exit")]
            options = [(fruit.fruit_name, fruit) for fruit in self.fruits]
            default_options.extend(options)
            choice = menu_generator(default_options, "Choose what Fruit you would like to remove.")
            if choice == "Exit":
                break
            self.fruits.remove(choice)
                
    def edit_fruit(self):
        while True:
            fruit_default = [("Exit Pick Fruit to Edit Menu", "Exit")]
            fruit_options = [(fruit.fruit_name, fruit) for fruit in self.fruits]
            fruit_default.extend(fruit_options)
            fruit_choice = menu_generator(fruit_default, "Choose what Fruit you would like to edit.")
            if fruit_choice == "Exit":
                break
            while True:
                edit_options = [("Exit Edit Fruit Menu", "Exit"), ("Edit Name", "Name"), ("Edit Description", "Desc"), ("Edit Type", "Type"),
                                ("Edit Raffle Weight", "Weight"), ("Toggle Availability", "Availabilty"), ("Add Ability", "Add A"),
                                ("Remove Ability", "Remove A")]
                edit_choice = menu_generator(edit_options, f"{fruit_choice}\nChoose what part of the fruit to edit.")
                if edit_choice == "Exit":
                    index = self.fruits.index(fruit_choice)
                    self.fruits[index] = fruit_choice
                    break
                elif edit_choice == "Name":
                    fruit_choice.fruit_name = input_validator("default", "Please input the Fruit's new Name: ")
                elif edit_choice == "Desc":
                    fruit_choice.fruit_desc = input_validator("default", "Please input the Fruit's new Description: ")
                elif edit_choice == "Type":
                    fruit_choice.type = input_validator("default", "Please input the Fruit's Type: ")
                elif edit_choice == "Weight":
                    fruit_choice.weight = input_validator("number", "Please input the Fruit's raffle Weight: ")
                elif edit_choice == "Availabilty":
                    if fruit_choice.available:
                        fruit_choice.available = False
                    else:
                        fruit_choice.available = True
                elif edit_choice == "Add A":
                    ability = {}
                    ability["ability_name"] = input_validator("default", "Please input the Ability's Name: ")
                    ability["ability_desc"] = input_validator("default", "Please input the Ability's Description: ")
                    new_ability = Ability(ability)
                    user = menu_generator([("Yes", True), ("No", False)], "Keep and add this new Ability?\n" + str(new_ability))
                    if user:
                        fruit_choice.abilities.append(new_ability)
                elif edit_choice == "Remove A":
                    while True:
                        options_default = [("Exit Remove Ability Menu", "Exit")]
                        options = [(ability.ability_name, ability) for ability in fruit_choice.abilities]
                        options_default.extend(options)
                        choice = menu_generator(options_default, "Choose what Ability you would like to remove.")
                        if choice == "Exit":
                            break
                        fruit_choice.abilities.remove(choice)
                        
    def raffle_fruit(self):
        while True:
            available_fruit = []
            fruit_weight = []
            for fruit in self.fruits:
                if fruit.available:
                    available_fruit.append(fruit)
                    fruit_weight.append(fruit.weight)
            if not available_fruit:
                break

            chosen = random.choices(available_fruit, fruit_weight, k = 1)[0]
            input(str(chosen)+"Press ENTER to continue.")
            user = menu_generator([("Remove from Avaiable Fruit", "Remove"), ("Keep in Avaiable", "Keep")], "Do you want to keep the fruit in avaiable?")
            if user == "Remove":
                index = self.fruits.index(chosen)
                self.fruits[index].available = False
            user = menu_generator([("Yes", False), ("No", True)], "Do you want to draw again?")
            if user:
                break

    def view_fruit(self):
        while True:
            default_options = [("Exit Fruit Viewer", "Exit")]
            options = [(fruit.fruit_name, fruit) for fruit in self.fruits]
            default_options.extend(options)
            
            choice = menu_generator(options, "Choose what Fruit you would like to view.")
            if choice == "Exit":
                break
            input(str(choice)+"\nPress ENTER to continue.\n")
            
            

    def export(self):
        file = {}
        file["name"] = self.file_name
        file["fruits"] = []
        for fruit in self.fruits:
            file["fruits"].append(fruit.export())
        return file