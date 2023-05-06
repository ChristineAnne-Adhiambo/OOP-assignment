class Student:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def show_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def year_of_birth(self):
        current_year = 2023  
        return current_year - self.age

    def show_initials(self):
        return f"{self.first_name[0]}.{self.last_name[0]}"


student = Student("Christine", "Adhiambo", 24, "Kenya")
full_name = student.show_full_name()
print(full_name)  

birth_year = student.year_of_birth()
print(birth_year)

initials = student.show_initials()
print(initials) 
