class Road:

    def __init__(self, length, width):
        self._length, self._width = length, width

    @property
    def weight_asphalt(self):
        return round(self._length * self._width * 25 * 5 / 1000, 2)


new_road = Road(20, 5000)
print(new_road.weight_asphalt)
