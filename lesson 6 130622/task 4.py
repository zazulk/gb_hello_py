from random import randint
from random import choice


class Car:
    speed = 40
    color = "\033[30m"
    name = "Car"
    is_police = False

    def __init__(self, speed, color, name, is_police=False):
        self.speed, self.color, self.name, self.is_police = speed, color, name,\
                                                            is_police

    def go(self):
        print("\tПогнали!")

    def stop(self):
        print("\tТормози.")

    def turn(self, direction):
        print(f"\tДвигай {direction}!")

    def show_speed(self):
        print(f"\tСкорость: {self.speed}км/ч.")


class TownCar(Car):
    pic = "🚙"

    def go(self):
        print("\tГазку!")

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"\t🚨 Нарушаем, нарушаем! Превышение на \033[31m{self.speed - 60}\033[0mкм")


class SportCar(Car):
    pic = "🏎"

    def go(self):
        print("\tТапку в пол!")


class WorkCar(Car):
    pic = "🚛"

    def go(self):
        print("\tГазуй!")

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"\t🚨 Нарушаем, нарушаем! Превышение на \033[31m{self.speed - 40}\033[0mкм")


class PoliceCar(Car):
    pic = "🚓"

    def __init__(self, speed, color, name):
        self.color = "\033[47m\033[34m"
        super().__init__(speed, self.color, name, is_police=True)


def car_factory(car_type):
    colors = [
        "\033[41m\033[30m",
        "\033[42m\033[30m",
        "\033[43m\033[30m",
        "\033[45m\033[30m",
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
    example = res_type.get("class")(speed=res_speed, color=choice(colors),
                                    name=choice(res_type.get("names")))
    return example


for el in ["sport", "town", "police", "work"]:
    car = car_factory(el)
    print(f"{car.pic} {car.color}\033[1m {car.name} \033[0m")
    car.go()
    car.show_speed()
    car.stop()
    car.turn(choice(["налево", "направо", "прямо"]))
    print("-" * 30)
