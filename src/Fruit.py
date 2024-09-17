class Fruit:
    def __init__(self, name, fruit_type, weight, desc, abilities = None, available = True) -> None:
        self.name = name
        self.fruit_type = fruit_type
        self.weight = int(weight)
        self.desc = desc
        self.avaiable = available
        self.abilities = []
        if abilities:
            for ability in abilities:
                self.abilities.append(Ability(ability["ability_name"], ability["ability_desc"]))

        
    def edit_name(self, new_name):
        self.name = new_name
        
    def edit_fruit_type(self, new_fruit_type):
        self.fruit_type = new_fruit_type
        
    def edit_weight(self, new_weight):
        self.weight = new_weight
    
    def edit_desc(self, new_desc):
        self.desc = new_desc
        
    def add_ability(self, name, desc):
        if self.abilities.count(name) < 1:
            self.abilities.append(Ability(name, desc))
        
    def del_ability(self, ability_obj):
        if self.abilities.count(ability_obj) > 0:
            self.abilities.remove(ability_obj)
            
    def toggle_avaiable(self):
        if self.avaiable:
            self.avaiable = False
        else:
            self.avaiable = True
        
    def export(self):
        abilities = [ability.export() for ability in self.abilities]
        return {"fruit_name": self.name, "type": self.fruit_type, "weight": self.weight, "fruit_desc": self.desc, "abilities": abilities, "available" : self.avaiable}

    def __str__(self) -> str:
        string = ""
        string += f"Name: {self.name}\n"
        string += f"Type: {self.fruit_type}\n"
        string += f"Desc: {self.desc}\n"
        string += f"Weight: {self.weight}\n"
        string += f"Can be drawn: {self.avaiable}\n"
        string += f"\nAbilities:\n"
        for ability in self.abilities:
            string += f"\tAbility Name: {ability.name}\n"
            string += f"\tAbility Desc: {ability.desc}\n\n"
        return string
        
class Ability:
    def __init__(self, name, desc) -> None:
        self.name = name
        self.desc = desc
        
    def edit_name(self, new_name):
        self.name = new_name
        
    def edit_desc(self, new_desc):
        self.desc = new_desc
        
    def export(self):
        return {"ability_name": self.name, "ability_desc": self.desc}