# list of cars
list_of_cars = [
   {'id_num': 1, 'make': 'Nissan', 'model': 'Pathfinder', 'year': 2024, 'mileage': 54321, 'services': 'none'},
   {'id_num': 2, 'make': 'Toyota', 'model': 'Camry', 'year': 2025, 'mileage': 4321, 'services': 'none'},
   {'id_num': 3, 'make': 'Dodge', 'model': 'Neon', 'year': 1999, 'mileage': 654321, 'services': 'New Engine'}
]
    
car_instances = []

for car in list_of_cars:
    car_instances.append(
        Cars(
            id_num = car.get('id_num'), 
            make = car.get('make'), 
            model = car.get('model') , 
            year = car.get('year'), 
            mileage = car.get('mileage'), 
            services = car.get('services')
         )
    )
    

print(car_instances)  