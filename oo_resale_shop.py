from computer import *

class ResaleShop:

    # What attributes will it need?

    inventory: list

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # What methods will you need?
    def buy(self, computer):
        """ Method for buying a computer for the shop
            
            Inputs computer
            
            Returns item_id"""

        #Adds computer to store inventory and prints the computer being bought
        #and prints the inventory 
        self.inventory.append(computer)
        print(f'Buying{computer.description}')
        self.print_inventory()

        #Sets the idx of the computer to item_id and then returns it
        item_id = self.inventory.index(computer)
        return item_id
    
    def sell(self, computer, item_id: int):
        """ Method for selling a computer from the shop
        
            Inputs computer and item_id"""
        
        #if there is a computer in the inventory
        if self.inventory[item_id]:

            #deletes the item from the inventory and prints it being sold
            del self.inventory[item_id]
            print(f'Selling {computer.description}')
            print(f'Sold.')
        
        #else nothing in inventory
        else:
            
            #prints that the item doesn't exist
            print(f'Item does not exist')
    
    def refurbish(self, computer, item_id, new_os = None):
        """ Method for refurbishing an old computer 
            
            Inputs computer, item_id, and new_os"""
        
        #if there is a computer in the inventory
        if self.inventory[item_id] is not None:

            #find the idx of the proper computer 
            computer = self.inventory[item_id]
        
        #if the computer is older than the year 2000 it's price is set to
        #zero it cannot be sold and must be donated
        if int(computer.year_made) < 2000:
            computer.update_price(0)
        
        #elif the computer is older than 2012 it is discounted 
        #to $250
        elif int(computer.year_made) < 2012:
            updated = computer.update_price(250)
        
        #elif the computer is older than 2018 the price is 
        #discounted to $550
        elif int(computer.year_made) < 2018:
            computer.update_price(550)
        
        #else the computer price is $1000
        else:
            computer.update_price(computer, 1000)
        
        #if the computer needs a new operating system then
        #update the operating system of the computer
        if new_os is not None:
            computer.update_os(computer, new_os)
        
        #else print that the item is not found and select another 
        #to refurbish
        else:
            print("Item", item_id, "not found. Select another item to refurbish.")
        
        #print that the computer is refurbished and print the inventory
        print(f'Refurbished!')
        self.print_inventory()
    
    def print_inventory(self):
        """ Method for printing the details of the computers in the stores inventory"""

        #if there is a computer in the inventory
        if self.inventory:
            
            #for computers in the inventory
            for i in self.inventory:

                #print the computers information
                print(f'Item ID:{self.inventory.index(i)} : description: {i.description}, processor_type: {i.processor_type}, hard_drive_capacity: {i.hard_drive_capacity}, memory: {i.memory}, operating_system: {i.operating_system}, year_made: {i.year_made}, price: {i.price}')
        
        #else print that the inventory is empty 
        else:
            print(f'Inventory is empty')

def main():

    #new computer information 
    new_computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)

    #creates the shop 
    myShop: ResaleShop = ResaleShop()

    #buys the new computer and sets its item_id
    item_id = myShop.buy(new_computer)

    #refurbishs the computer with a new operating system
    myShop.refurbish(new_computer, item_id, "MacOS Monterey")

    #sells the new computer
    myShop.sell(new_computer, item_id)

main()