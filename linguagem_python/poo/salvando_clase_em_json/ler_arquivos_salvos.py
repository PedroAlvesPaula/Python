import json
from salvando_dados_de_uma_classe import FILE_PATH

class Car:
    def __init__(self, name, model, color, motor):
        self.name = name
        self.model = model
        self.color = color
        self.motor = motor

def grab_saved_informations():
    informations = {}

    try:
        with open(FILE_PATH, 'r') as file:
            informations = json.load(file)
    except: 
        print("No information in the saved file")
    finally:
        return informations

data_car = grab_saved_informations()

if data_car:
    car1 = Car(**data_car)
    print(car1.name)
    print(car1.model)
    print(car1.color)
    print(car1.motor)
