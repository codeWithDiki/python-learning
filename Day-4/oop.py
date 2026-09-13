from classes.example_class import Person, Hobby

x = Person()

print(f"Person Data : {x.getData()}")

x.updatePersonAge(27)

print(f"Updated Person Data : {x.getData()}")

y = Hobby()

print(f"Person Data from Hobby : {y.getData()}")

y.postHobby("Makar")

hobbies = y.getPersonWithHobby()

print(f"Person with Hobbies : {hobbies}")


# Inheritance encapsulation error example
# y.updatePersonAge(27)

# print(f"Person Data from Hobby : {y.getData()}")


    