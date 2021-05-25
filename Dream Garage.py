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
    if len(garage) == 0:
        answer = input("Would you like to add your first car? Y/N")
        if answer == "Y":
            add_car()

def greeting():
    print("Welcome to Dream Garage Builder. This program will help you track your Dream 3 car garage.")

def add_car():
    if len(garage) <= 3:
        model_name = input("What is the model name you would like to add?")
        new_car = Car(model_name)
        additional_info = input("What other info would you like to add? Brand, Year, Price, Category.")
        additional_info = additional_info.lower()
        if "brand" in additional_info:
            new_car.brand = input("Please enter brand name: ")
        if "year" in  additional_info:
            new_car.year = input("Please enter model year: ")
        if "price" in additional_info:
            new_car.price = input("Please enter vehicle price: $")
        if "category" in additional_info:
            new_car.category = input("Please enter vehicle category: (Ex. Sport, Luxury, SUV)")
        cars[new_car.model] = [new_car.brand, new_car.year, new_car.price, new_car.category]
        print("Successfully added {new_car} to garage.".format(new_car = new_car.model))
    else:
        print("Please remove an exsisting vehicle to add another vehicle.")


dream_garage()