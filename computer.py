class Computer:

    # What attributes will it need?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):

        #creates the computer
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    # What methods will you need?
    def update_os(self, computer, update: str):
        """ Method for updating the operating system of the computer"""

        #Updates from the old operating system to the new one
        self.operating_system = update

    def update_price(self, new_price: int):
        """Method for updating the price of the computer"""

        #updates the old price to the new price
        self.price = new_price