class Car:
    def __init__(self, model, brand = None, year = None, price = None, category = None):
        self.model = model
        self.brand = brand
        self.year = year
        self.price = price
        self.category = category

garage = {}

def dream_garage():
    greeting()
    answer = ""
    while answer != "N":
        answer = input("Would you like to add a vehicle? Y/N \n")
        if answer == "Y":
            add_car()
    
    goodbye()
    

def greeting():
    print("Welcome to Dream Garage Builder. This program will help you track your Dream 3 car garage.")

def goodbye():
    print("Thank you for using my Dream Garage Builder.")

def view_garage(garage):
    for car, values in garage.items():
        print(car, ":", values)

def add_car():
    if len(garage) < 3:
        model_name = input("What is the model name you would like to add? \n")
        new_car = Car(model_name)
        additional_info = input("What other info would you like to add? Brand, Year, Price, Category. \n")
        additional_info = additional_info.lower()
        if "brand" in additional_info:
            new_car.brand = input("Please enter brand name: ")
        if "year" in  additional_info:
            new_car.year = input("Please enter model year: ")
        if "price" in additional_info:
            new_car.price = input("Please enter vehicle price: $")
        if "category" in additional_info:
            new_car.category = input("Please enter vehicle category: (Ex. Sport, Luxury, SUV) \n")
        garage[new_car.model] = [new_car.brand, new_car.year, new_car.price, new_car.category]
        print("Successfully added {new_car} to garage.".format(new_car = new_car.model))
    else:
        print("Please remove an exsisting vehicle to add another vehicle.")
        ans = input("Would you like to remove a vehicle? Y/N \n")
        if ans == "Y":
            vehicle = input("Please enter the vehicle model or 'garage' to view current vehicles. \n")
            if vehicle == 'garage':
                view_garage(garage)
            else:
                if vehicle in garage.keys():
                    remove_car(vehicle)
                else:
                    print("Could not find specified vehicle in garage.")
    view_g = input("Would you like to view your garage? Y/N \n")
    if view_g =="Y":
        view_garage(garage)

                    

def remove_car(model):
    garage.pop(model)
    print("{} successfully removed from garage.".format(model))

dream_garage()