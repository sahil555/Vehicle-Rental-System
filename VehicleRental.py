import datetime,random

class Vehicle:
    inventorylist = []

    def __init__(self,typeofvehicle,license_no,rentedornot):
        self.inventorylist.append([typeofvehicle, license_no , rentedornot,None] )    

    def displayvehicle(self):
        for i in self.inventorylist:
            print(i)

    def rentvehicle(self,license_no,name):
        for i in self.inventorylist:
            if str(license_no) in i[1]:
                i[2] = True
                i[3] = name



    def returnvehicle(self,rentaltime,license_no,rentalbasis):
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

        if rentaltime:
            now = datetime.datetime.now()
            print(rentaltime,now)
            rentalperiod = now - rentaltime

                
            # daily bill calculation
            if rentalbasis == 1800:
                bill = round(rentalperiod.days) * 1800 
                
            # weekly bill calculation
            elif rentalbasis == 9000:
                bill = round(rentalperiod.days / 7) * 9000
            
               

            print("Thanks for returning your Vehicle. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you have rented a Vehicle with us?")
            return None



    
   

class Customer:
    rentedvehicle = []

    def __init__(self,name):
        self.name = name
        self.rentaltime = ''
        self.rentalbasis = ''
        self.vehicle = ''
    
    def requestvehicle(self,rentalbasis,day):
        """
        Takes a request from the customer for the number of Vehicles.
        """
                      
        vehicle = input("Enter Vehicle's License Number: ")
        

        if vehicle in self.rentedvehicle:
            print("This is already Rented Vehicle")
        else:
            self.rentedvehicle.append([vehicle,day,rentalbasis])
        return (vehicle)


     
    def requestrentedvehicle(self):
        if self.rentedvehicle:
            for i in self.rentedvehicle:
                print(i)
        else:
            print('You have not rented any Vehicle')


    def returnvehicle(self):

        vehicle = input("Enter Vehicle's License Number: ")
        
        for i in self.rentedvehicle:
            if vehicle in i:
                self.rentaltime = i[1]
                self.rentalbasis = i[2]
                self.vehicle = [0]
                self.rentedvehicle.remove(i)

                print("you have Successfully return vehicle!")
                return self.rentaltime
                
            else:
                print("You have never rented this vehicle!")
        
     

   
        

    