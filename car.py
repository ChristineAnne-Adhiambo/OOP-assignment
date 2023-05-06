class Car:
    brand = "Toyota"

    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def start_engine(self):
        return f"The {self.model}'s engine is running."

    def honk(self):
        return "Beep beep!"

    def get_car_info(self):
        return f"{self.year} {self.color} {self.brand} {self.model}"
