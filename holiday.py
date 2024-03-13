city_flight={"birmingham": 100,
             "manchester": 120,
             "belfast": 150,
             "cardiff": 180,
             "moscow": 300,
             "tokyo": 400,
             "new york": 400,
             "riga": 100}

one_night=50
day_car=25
num_nights=0
flight=0
car=0
car_price=0
holiday=0
hotel=0

def hotel_cost():
    try:
        print("")
        num_nights=int(input("Enter number of nights you will be staying at hotel:"))
        if num_nights > 0:
            hotel = num_nights * one_night
            print(f"Whole price for the hotel will be: £{hotel}\n")
        else:
            if num_nights <= 0:
                print("Invalid input! Enter positive non-null number!")
    except ValueError:
        print("Invalid input!")
    return hotel

def plane_cost():
    try:
        item=input("Enter the city you flying to: ").lower()
        if item in city_flight:
            flight=city_flight[item]
            print(f"Price for the flight from London will be: £{flight}\n")
        else:
            print("We don't fly to such destinations!")
    except ValueError:
        print("Invalid input!")
    return flight
        
def car_rental():
    try:
        car=int(input("Enter number of days for which you will be hiring car: "))
        if car > 0:
            car_price = car * day_car
            print(f"Price for the car hire will be: £{car_price}\n")
        else:
            if car <= 0:
                print("Invalid input! Enter positive non-null number!")
    except ValueError:
        print("Invalid input!")
    return car_price

def holiday_cost():
    holiday=hotel_cost()+plane_cost()+car_rental()
    print(f"Whole price for your holiday will be: £{holiday}\n\n")

holiday_cost()