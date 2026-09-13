class Person :
    name = "Diki"
    age = 26
    # Encapsulations Private Property
    __quote = "Hiduplah seperti larry"
    
    def __init__(self):
        pass
    
    def getData(self) :
        return {
            "name" : self.name,
            "age" : self.age
        }
        
    def getQuote(self):
        return self.__quote
    
    def updatePersonAge(self, age) : 
        self.__updateAge(age)
    
    # Encapsulation Private Class Method
    def __updateAge(self, age):
        self.age = age
        
        
class Hobby(Person):
    hobbies = []
    
    def __init__(self):
        super().__init__()
    
    def postHobby(self, hobby):
        self.hobbies.append(hobby)
        
    def getPersonWithHobby(self):
        return self.getData() | {
            "hobbies" : self.hobbies
        }
        
    def updatePersonAge(self, age) :
        self.__updateAge(age)
    