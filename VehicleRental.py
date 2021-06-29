import datetime,random

class Vehicle:
    inventorylist = []

    def __init__(self,typeOfvehicle,license_no,rentedOrNot):
        self.inventorylist.append([typeOfvehicle, license_no , rentedOrNot,None] )    

    def displayVehicle(self):
        for i in self.inventorylist:
            print(i)

    def rentvehicle(self,license_no,Name):
        for i in self.inventorylist:
            if str(license_no) in i[1]:
                i[2] = True
                i[3] = Name



    def returnvehicle(self,rentalTime,license_no,rentalBasis):
        """
        1. Accept a rented Vehicle from a customer
        2. Replensihes the inventory
        3. Return a bill
        """

        for i in self.inventorylist:
            if str(license_no) in i[1]:
                i[2] = False
                i[3] = None



        bill = 0

        if rentalTime:
            now = datetime.datetime.now()
            print(rentalTime,now)
            rentalPeriod = now - rentalTime

                
            # daily bill calculation
            if rentalBasis == 20:
                bill = round(rentalPeriod.days) * 20 
                
            # weekly bill calculation
            elif rentalBasis == 60:
                bill = round(rentalPeriod.days / 7) * 60
            
               

            print("Thanks for returning your Vehicle. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you have rented a Vehicle with us?")
            return None



    
   

class Customer:
    rentedVehicle = []

    def __init__(self,Name):
        self.Name = Name
        self.rentalTime = ''
        self.rentalBasis = ''
        self.vehicle = ''
    
    def requestvehicle(self,rentalBasis,day):
        """
        Takes a request from the customer for the number of Vehicles.
        """
                      
        vehicle = input("Enter Vehicle's License Number: ")
        

        if vehicle in self.rentedVehicle:
            print("This is already Rented Vehicle")
        else:
            self.rentedVehicle.append([vehicle,day,rentalBasis])
        return (vehicle)


     
    def requestrentedvehicle(self):
        if self.rentedVehicle:
            for i in self.rentedVehicle:
                print(i)
        else:
            print('You have not rented any Vehicle')


    def returnvehicle(self):

        vehicle = input("Enter Vehicle's License Number: ")
        
        for i in self.rentedVehicle:
            if vehicle in i:
                self.rentalTime = i[1]
                self.rentalBasis = i[2]
                self.vehicle = [0]
                self.rentedVehicle.remove(i)

                print("you have Successfully return vehicle!")
                return self.rentalTime
                
            else:
                print("You have never rented this vehicle!")
        
     

   
        

    