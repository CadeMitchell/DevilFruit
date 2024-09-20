from .ability import Ability

class Fruit:
    def __init__(self, file: dict) -> None:
        self.fruit_name = file["fruit_name"]
        self.fruit_desc = file["fruit_desc"]
        self.weight = file["weight"]
        self.type = file["type"]
        self.avaliable = file["available"]
        self.abilities = []
        if file["abilities"]:
            for ability in file["abilities"]:
                self.abilities.append(Ability(ability))
                
    def export(self):
        export = {"fruit_name": self.fruit_name,
                  "fruit_desc": self.fruit_desc,
                  "type": self.type,
                  "weight": self.weight,
                  "available": self.avaliable,
                  "abilities": []}
        if self.abilities:
            for ability in self.abilities:
                export["abilities"].append(ability.export())
        return export
    
    def display_fruit(self):
        print(f"Name: {self.fruit_name}")
        print(f"Desc: {self.fruit_desc}")
        print(f"Type: {self.type}")
        print(f"Weight: {self.weight}")
        print(f"Avaiable: {self.abilities}")
        if self.abilities:
            for ability in self.abilities:
                ability.display_ability()
        