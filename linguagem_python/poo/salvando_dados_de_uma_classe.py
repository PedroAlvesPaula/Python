import json

FILE_PATH = './/data_car.json'

class car:
    def __init__(self, name, model, color, motor) -> None:
        self.name = name
        self.model = model
        self.color = color
        self.motor = motor

def save_in_json(file_data):
    with open(FILE_PATH, 'w') as file:
        json.dump(file_data, file, indent=2)

corsa = car('Argo', 'fire', 'Black', 'motor ap 1000')

corsa_data = corsa.__dict__
try:
    save_in_json(corsa_data)
except:
    print(corsa_data)
