# DRAFT
# TODO: доделать или переделать полностью 😩
class OfficeEquipment:
    name: str
    brand: str
    model: str

    def __init__(self, name="Оргтехника", brand=None, model=None):
        self.name, self.brand, self.model = name, brand, model

    def __str__(self):
        return "".join([f"\t{key}: {val}\n" for key, val in
                        self.__dict__.items()])

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def get_params(obj):
        return obj.__dict__.keys()


class GraphicsEquipment(OfficeEquipment):
    color: str
    max_format: str
    type_sys: str
    is_color: bool

    def __init__(self, name, brand, model, color, max_format, type_sys, is_color):
        self.color, self.max_format = color, max_format
        self.type_sys, self.is_color = type_sys, is_color
        super().__init__(name, brand, model)


class Printer(GraphicsEquipment):
    name = "принтер"
    speed: int
    speed_units = "стр./мин."

    def __init__(self, brand=None, model=None, color=None, max_format=None,
                 type_sys=None, speed=None, speed_units=None, is_color=False):

        self.speed, self.speed_units = speed, speed_units
        super().__init__(name=Printer.name, brand=brand, model=model, color=color,
                         max_format=max_format, type_sys=type_sys,
                         is_color=is_color)


class Copier(GraphicsEquipment):
    name = "копир"
    speed: int
    speed_units = "коп./мин."

    def __init__(self, brand=None, model=None, color=None, max_format=None,
                 type_sys=None, speed=None, speed_units=None, is_color=False):
        self.speed, self.speed_units = speed, speed_units
        super().__init__(name=Copier.name, brand=brand, model=model,
                         color=color,
                         max_format=max_format, type_sys=type_sys,
                         is_color=is_color)


class Scanner(GraphicsEquipment):
    name = "сканер"
    # разрешение
    resolution: str
    resolution_units = "DPI"

    def __init__(self, brand=None, model=None, color=None, max_format=None,
                 type_sys=None, resolution=None, resolution_units=None, is_color=False):
        self.resolution, self.resolution_units = resolution, resolution_units
        super().__init__(name=Scanner.name, brand=brand, model=model,
                         color=color,
                         max_format=max_format, type_sys=type_sys,
                         is_color=is_color)


class OfficeEquipmentStorage:
    def __init__(self):
        self.equipments = []

    def add_equipment(self, equip: OfficeEquipment, office_unit=None):
        unit_info = {"office_unit": office_unit}
        # self.equipments.append({**equip.__dict__, **unit_info})
        self.equipments.append({"equip": equip, **unit_info})

    def find_equipment(self, kwargs):
        search_params = dict((k, v) for k, v in kwargs.items() if v)
        res = []
        for el in self.equipments:
            is_fit = True
            for key, val in search_params.items():
                if key == "office_unit":
                    if el["office_unit"].lower() != val.lower():
                        is_fit = False
                        continue
                atr = getattr(el["equip"], key)
                if not atr or atr.lower() != val.lower():
                    is_fit = False
                    continue
            if is_fit:
                res.append(el)
        return res

    def move_equipment(self, office_unit, search_params):
        found = self.find_equipment(search_params)[0]
        if found:
            found["office_unit"] = office_unit
        else:
            print("Не нашел оборудование в базе")

    def remove_equipment(self, search_params):
        found = self.find_equipment(search_params)[0]
        if found:
            self.equipments.remove(found)
        else:
            print("Не нашел оборудование в базе")


new_printer = Printer(brand="Canon")
print(new_printer)
new_scanner = Scanner(brand="EPSON")
print(new_scanner)
print("-" * 30)
storage = OfficeEquipmentStorage()
storage.add_equipment(new_printer, "Бухгалтерия")
storage.add_equipment(new_scanner, "Бухгалтерия")
print(storage.equipments)
print("-" * 30)
# print(storage.find_equipment(name="сканер"))
print(storage.find_equipment({"color": "black"}))
print("-" * 30)
storage.move_equipment("HR-отдел", {"name": "сканер"})
print(storage.equipments)

