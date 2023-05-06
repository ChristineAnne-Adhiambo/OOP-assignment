class Fruit:
    family = "Rosaceae"

    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste

    def is_delicious(self):
        if self.taste == "sweet":
            return True
        else:
            return False

    def describe(self):
        return f"The {self.name} is {self.color} and tastes {self.taste}."

    def get_family(self):
        return self.family
