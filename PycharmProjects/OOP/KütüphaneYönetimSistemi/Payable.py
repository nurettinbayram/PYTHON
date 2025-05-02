from abc import ABC, abstractmethod


class Payable(ABC):
    @abstractmethod
    def pay_fee(self, amount):
        pass