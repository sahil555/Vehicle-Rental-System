from VehicleRental import  Customer, Vehicle
import random,uuid, datetime
def main():
    vtype = ["Mini","Sedan","SUV","Luxury"]
    for i in range(1,20):
        inventory = Vehicle(vtype[random.randint(0, 3)], str(uuid.uuid4()) , False)
    
    customer = Customer(input("Enter Your Name  : "))

    while True:
        print(f'\n        ********* Welcome {customer.Name} ********* ')
        print("""
        ====== Vehicle Rental System =======
        1. Display available Vehicle
        2. Display Rented Vehicle
        3. Request a Vehicle on daily basis $20
        4. Request a Vehicle on weekly basis $60
        5. Return a Vehicle
        6. Exit
        """)
        
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        
        if choice == 1:
            inventory.displayVehicle()
        
        elif choice == 2:
            customer.requestrentedvehicle()

        elif choice == 3:
            inventory.rentvehicle(customer.requestvehicle(20, datetime.datetime.now()),customer.Name)

        elif choice == 4:
            inventory.rentvehicle(customer.requestvehicle(60, datetime.datetime.now()),customer.Name)
            
        elif choice == 5:
            customer.bill = inventory.returnvehicle(customer.returnvehicle(),customer.vehicle,customer.rentalBasis)
        elif choice == 6:
            break
        else:
            print("Invalid input. Please enter number between 1-6 ")        
    print("Thank you for using the Vehicle rental system.")


if __name__=="__main__":
    main()