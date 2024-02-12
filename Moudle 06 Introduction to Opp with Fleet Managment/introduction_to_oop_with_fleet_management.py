class Company:
    def __init__(self, name) -> None:
        self.name = name
        self.buses = []
        self.routes = []
        self.drivers = []
        self.managers = []
        self.supervisors = []
    
    def add_bus(self, bus):
        self.buses.append(bus)
    
    def add_route(self, route):
        self.routes.append(route)
    
    def add_driver(self, driver):
        self.drivers.append(driver)
    
    def add_manager(self, manager):
        self.managers.append(manager)
    
    def add_supervisor(self, supervisor):
        self.supervisors.append(supervisor)

class Driver:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Driver: {self.name}, Age: {self.age}"

class Bus:
    def __init__(self, serial) -> None:
        self.serial = serial
    
    def __str__(self):
        return f"Bus: {self.serial}"

class Route:
    def __init__(self, frm, to) -> None:
        self.from_location = frm
        self.to_location = to
    
    def __str__(self):
        return f"Route: From {self.from_location} to {self.to_location}"

class Manager:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Manager: {self.name}, Age: {self.age}"

class Supervisor:
    def __init__(self, name) -> None:
        self.name = name
    
    def __str__(self):
        return f"Supervisor: {self.name}"


company = Company("XYZ Transport")
bus = Bus("1234")
route = Route("A", "B")
driver = Driver("John", 30)
manager = Manager("Alice", 40)
supervisor = Supervisor("Bob")

company.add_bus(bus)
company.add_route(route)
company.add_driver(driver)
company.add_manager(manager)
company.add_supervisor(supervisor)

for obj_list in [company.buses, company.routes, company.drivers, company.managers, company.supervisors]:
    for obj in obj_list:
        print(obj)
