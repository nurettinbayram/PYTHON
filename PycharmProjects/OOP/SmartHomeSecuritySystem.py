from abc import ABC, abstractmethod


class Device(ABC):
    def __init__(self, name, status):
        self.name = name
        self.status = status


class Connectable(ABC):
    @abstractmethod
    def connection(self):
        pass


class Detectable(ABC):
    @abstractmethod
    def dedector(self):
        pass


class Alarmable(ABC):
    @abstractmethod
    def alarm(self):
        pass


class MotionSensor(Detectable, Connectable, Device):
    def __init__(self, name, status):
        super().__init__(name, status)

    def connection(self):
        print(self.name, " connected wifi!!!")

    def dedector(self):
        print(self.name, " dedected something!!!")


class DoorSensor(Device, Detectable, Connectable):
    def __init__(self, name, status):
        super().__init__(name, status)

    def connection(self):
        print(self.name, " connected wifi!!!")

    def dedector(self):
        print(self.name, " dedected something!!!")


class Siren(Device, Alarmable):
    def __init__(self, name, status):
        super().__init__(name, status)

    def alarm(self):
        print(self.name, " is sirening!!!")


class SmartAlarm(Device, Alarmable, Connectable):
    def __init__(self, name, status):
        super().__init__(name, status)

    def connection(self):
        print(self.name, " connected wifi!!!")

    def alarm(self):
        print(self.name, " set!!!")


devises = [MotionSensor("motionsensor1", False), DoorSensor("doorsensor1", False),
           Siren("siren1", True), SmartAlarm("smartalarm1", True),
           DoorSensor("doorsensor", True)]

abilities = {
    Connectable: lambda obj: obj.connection(),
    Detectable: lambda obj: obj.dedector(),
    Alarmable: lambda obj: obj.alarm()
}

for devise in devises:
    print(f"**********{devise.name}**********")
    for interface, action in abilities.items():
        if isinstance(devise, interface) and devise.status:
            action(devise)
    print()
