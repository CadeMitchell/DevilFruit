class Fruit:
    def __init__(self, name, fruit_type, weight, desc) -> None:
        self.name = name
        self.fruit_type = fruit_type
        self.weight = weight
        self.desc = desc
        self.avaiable = True
        self.abilities = []
        
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
        
    def del_ability(self, name):
        if self.abilities.count(name) > 0:
            self.abilities.remove(name)
            
    def toggle_avaiable(self):
        if self.avaiable:
            self.avaiable = False
        else:
            self.avaiable = True
        
    def export(self):
        return {"fruit_name": self.name, "type": self.fruit_type, "weight": self.weight, "fruit_desc": self.desc, "abilities": self.abilities}

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