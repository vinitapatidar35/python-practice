class Car:# The Blueprint (The Class)

    no_of_tyres = 4 # class variable 
    
    def __init__(self, model, year , color, for_sale):
    # dunder methode double underscore, we need this method to create an object
        # self.model (Permanent Slot) = model (Temporary Input Data)
        self.model = model
        self.year = year 
        self.color = color
        self.for_sale = for_sale

#methods
# methods are action that obj can perform
    # We put 'self' here so the method can read this car's data
    def drive(self):
        print("You drive the car.")
        # self.model lets this method grab the specific model name
        print(f"The {self.color} {self.model} is driving! Vroom!")

    def stop(self):
        print("you stop the car.")
        print(f"{self.model} stops")

    def describe(self):
        print(f'''Color of car is: {self.color},
              model of a car is : {self.model},
              year of the car is : {self.year},
              is that car for sale: {self.for_sale}''')

# class variable = share among all instance of a class
# define outside the constructor
# allow you to share data among all objects created from that class 
    