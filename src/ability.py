class Ability:
    def __init__(self, file: dict) -> None:
        self.ability_name = file["ability_name"]
        self.ability_desc = file["ability_desc"]
        
    def export(self):
        return {"ability_name": self.ability_name, "ability_desc": self.ability_desc}
    
    def display_ability(self):
        print(f"Abilty Name: {self.ability_name}")
        print(f"Description: {self.ability_desc}")