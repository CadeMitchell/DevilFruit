"""
This module is for providing general utilities.
"""
import json
import os
import sys

def clear():
    '''
    Clears the Console
    '''
    os.system("cls")

def load_file(path = "") -> dict:
    counter = 0
    while counter < 3:
        try:
            if not path:
                path = menu_generator([(file, "saves\\" + file) for file in os.listdir("saves")])
            with open(path, "r") as file:
                return json.load(file)
        except Exception as e:
            input(f"Error Occured. If this keeps happening, program will exit after {2-counter} more attempts. (Press ENTER to continue.)\nError: {e}")
            counter += 1
            continue
    sys.exit("Failed to load file after 3 attempts. Exiting program to prevent a infinite loop.")

def save_file(file: dict, path = "saves"):
    with open(path + "\\" + file["name"] + ".json", "w") as json_file:
            json.dump(file, json_file, sort_keys=False, indent=4)

def menu_generator(options: list[tuple[str, object]], prompt = "") -> object:
        '''Generates a Menu from a list of tuples.

        Args:
            options (list[tuple[str, Callable]]): str is for the name of the option and object will be returned if the item is selected.
            prompt (str): Provides a prompt for the user in addition to the options.

        Returns:
            object: Returns the selected object.
        '''
        while True:
            clear()
            if prompt:
                print(prompt)
            for index, (option, _) in enumerate(options):
                print(f"({index + 1}) - {option}")
            try:
                choice = int(input("Select an option: "))
                if 1 <= choice <= len(options):
                    return options[choice - 1][1]
                else:
                    input("Invalid choice. Please try again.\n(Press ENTER to continue)")
            except ValueError:
                input("Invalid input. Please enter a number.\n(Press ENTER to continue)")
                
def input_validator(validate_type = "default", prompt = ""):
    while True:
        clear()
        try:
            user = input(prompt)
            if validate_type == "default":
                return user
            elif validate_type == "text":
                if not user.replace(" ", "").isalnum():
                    raise TypeError
                return user
            elif validate_type == "number":
                return int(user)
        except TypeError:
            input(f"Error when accepting input.\nYou input: {user}\nExpected input: {validate_type}\nPress ENTER to continue.")
        except:
            input("Uknown error try again.\nPress ENTER to continue.")
                