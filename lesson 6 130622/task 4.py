from random import randint
from random import choice


class Car:
    speed = 40
    color = "red"
    name = "Car"
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed, self.color, self.name, self.is_police = speed, color, name,\
                                                            is_police

    def go(self):
        print("Поехали!")

    def stop(self):
        print("Тормози.")

    def turn(self, direction):
        print(f"Двигай {direction}")

    def show_speed(self):
        print(f"Скорость: {self.speed}")


class TownCar(Car):
    pic = "🚙"

    def go(self):
        print("Газку!")

    def show_speed(self):
        if self.speed > 60:
            print(f"🚨 Нарушаем, нарушаем! Превышение {self.speed - 60}км")
        else:
            print(f"Скорость: {self.speed}")


class SportCar(Car):
    pic = "🏎"

    def go(self):
        print("Тапку в пол!")


class WorkCar(Car):
    pic = "🚛"

    def go(self):
        print("Газуй!")

    def show_speed(self):
        if self.speed > 40:
            print(f"🚨 Нарушаем, нарушаем! Превышение {self.speed - 40}км")
        else:
            print(f"Скорость: {self.speed}")


class PoliceCar(Car):
    pic = "🚓"


def car_generator(car_type):
    colors = [
        "\033[31m",
        "\033[32m",
        "\033[33m",
        "\033[34m",
    ]
    car_types = {
        "sport": {
            "speeds": [randint(80, 310) for s in range(20)],
            "names": ["Honda Civic Type R", "Nissan GT-R", "Toyota Trueno"],
            "class": SportCar
        },
        "town": {
            "speeds": [randint(20, 180) for s in range(20)],
            "names": ["Honda Civic", "Ford Focus", "Hundai Solaris",
                      "Volkswagen Polo"],
            "class": TownCar
        },
        "work": {
            "speeds": [randint(10, 90) for s in range(20)],
            "names": ["Камаз K5", "МАЗ 5440", "MAN TGX"],
            "class": WorkCar
        },
        "police": {
            "speeds": [randint(10, 90) for s in range(20)],
            "names": ["Ford Mondeo", "Renault Logan", "Lada Vesta",
                      "Skoda Octavia"],
            "class": PoliceCar
        }
    }
    res_type = car_types.get(car_type)
    res_speed = choice(res_type.get("speeds"))
    is_police = car_type == "police"
    example = res_type.get("class")(speed=res_speed, color=choice(colors),
                                    name=choice(res_type.get("names")),
                                    is_police=is_police)
    return example


for el in ["sport", "town", "police", "work"]:
    car = car_generator(el)
    print(f"{car.pic} {car.color}{car.name}\033[0m")
    print(f"is police: {car.is_police}")
    car.go()
    car.show_speed()
    car.stop()
    car.turn(choice(["налево", "направо", "прямо"]))
    print("-" * 30)
