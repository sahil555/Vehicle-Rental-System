from VehicleRental import  Customer, Vehicle
import random,uuid, datetime
def main():
    vtype = ["Mini","Sedan","SUV","Luxury"]
    for i in range(1,20):
        inventory = Vehicle(vtype[random.randint(0, 3)], str(uuid.uuid4()) , False)
    
    customer = Customer(input("Enter Your name  : "))

    while True:
        print(f'\n        ********* Welcome {customer.name} ********* ')
        print("""
        ====== Vehicle Rental System =======
        1. Display available Vehicle
        2. Display Rented Vehicle
        3. Request a Vehicle on daily basis Rs. 1800
        4. Request a Vehicle on weekly basis Rs. 9000
        5. Return a Vehicle
        6. Exit
        """)
        
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an Number you have selected !")
            continue
        
        if choice == 1:
            inventory.displayvehicle()
        
        elif choice == 2:
            customer.requestrentedvehicle()

        elif choice == 3:
            inventory.rentvehicle(customer.requestvehicle(1800, datetime.datetime.now()),customer.name)

        elif choice == 4:
            inventory.rentvehicle(customer.requestvehicle(9000, datetime.datetime.now()),customer.name)
            
        elif choice == 5:
            customer.bill = inventory.returnvehicle(customer.returnvehicle(),customer.vehicle,customer.rentalbasis)

        elif choice == 6:
            break

        else:
            print("Invalid input. Please enter number between 1-6 ")
                   
    print("Thank you for using the Vehicle rental system.")


if __name__=="__main__":
    main()