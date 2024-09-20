from .fruit import Fruit
from .utilities import *
class Fruit_Manager:
    def __init__(self, file: dict) -> None:
        self.file_name = file["file_name"]
        self.fruits = []
        if file["fruits"]:
            for fruit in file["fruits"]:
                self.fruits.append(Fruit(fruit))
            
    def add_fruit():
        pass
                
