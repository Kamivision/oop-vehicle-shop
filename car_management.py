from cars import Cars
import Test_info


Test_info.test_cars()
# Terminal Application that interacts with the car class
while True:
    mode = input("""
----  Welcome  ----
1. Add a car
2. View all cars
3. View total number of cars
4. See a car's details
5. Service a car
6. Update mileage
7. Quit
-------------------
Please select a number:
    """)
    if mode == '1':
        Cars.add_car_from_menu()
    elif mode == '2':
        print(Cars.all_cars)
    elif mode == '3':
        print(f"Total Cars: {Cars.total_cars}")
    elif mode == '4':
        
        # Cars.display_car_details(car_id)
        Cars.display_car_details()
        # print(car)
        # print(str(car))
    # elif mode == '5':
    # elif mode == '6':    
    elif mode == '7':
        break   
