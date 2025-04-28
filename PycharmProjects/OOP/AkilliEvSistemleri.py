from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, name, status):
        self.name=name
        self.status=status

    def turnOn(self):
        if not self.status:
            print(self.name, " opened!!!")
            self.status = True
        else:
            print(self.name, " alredy open!!!")

    def turnOff(self):
        if self.status:
            print(self.name, " closed!!!")
            self.status=False
        else:
            print(self.name, " alrady close!!!")

# I. interface
class Connectable(ABC):
    @abstractmethod
    def connect_internet(self):
        pass

# II. interface
class Soundable(ABC):
    @abstractmethod
    def play_sound(self):
        pass
    @abstractmethod
    def adjustValume(self):
        pass

# III. interface
class Recordable(ABC):
    @abstractmethod
    def record(self):
        pass

class Lamp(Device):
    pass

class Camera(Device, Recordable, Connectable):

    def record(self):
        print(self.name, " is recording...")

    def connect_internet(self):
        print(self.name, " connected wifi!!!")

class Speaker(Device, Soundable):

    def adjustValume(self):
        print(self.name, " rised valume!! ")

    def play_sound(self):
        print(self.name, " is paly sound")

class SmartAC(Device, Connectable):

    def connect_internet(self):
        print(self.name, " conneced wifi!!!")


devices = [Lamp("lamp1", False), Camera("camera1", True),
           Speaker("speaker1", False), SmartAC("smartAC1", False)]

abilities = {
    Connectable:[lambda obj:obj.connect_internet()],
    Soundable: [lambda obj:obj.play_sound(),lambda obj:obj.adjustValume()],
    Recordable: [lambda obj:obj.record()]
}

for device in devices:
    print(f"------------{device.name}------------")
    device.turnOn()
    for interface, actions in abilities.items(): #burada item almamizin sebebi ilgili indexteki tum icerigi alabilmemiz
        if isinstance(device, interface):
            for action in actions:# burada value degeri bir dizi oldugundan diziyi dolasmasi gerekiyor
                action(device)
    device.turnOff()
    print()

