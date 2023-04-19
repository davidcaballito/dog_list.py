class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.breed}, {self.age} years old)"
    

dog_list = [
    Dog('Max', 'Golden Retriever', 3),
    Dog('Buddy', 'Beagle', 2),
    Dog('Rocky', 'Bulldog', 5),
    Dog('Daisy', 'Labrador Retriever', 1),
    Dog('Bailey', 'German Shepherd', 4)
]

for dog in dog_list:
    print(dog)
