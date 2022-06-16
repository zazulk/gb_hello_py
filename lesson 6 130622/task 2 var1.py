from random import randint
from random import randrange


class Road:

    def __init__(self, length, width):
        self._length, self._width = length, width

    def get_weight_asphalt(self):
        return round(self._length * self._width * 25 * 5 / 1000, 2)

    @property
    def length(self):
        return self._length/1000

    @property
    def width(self):
        return self._width


new_road = Road(randint(5000, 20_000), randrange(6, 25, 6))
print(f"Для покрытия дороги длиной {new_road.length}км и шириной "
      f"{new_road.width}м понадобится {new_road.get_weight_asphalt()}т "
      f"асфальта.")
