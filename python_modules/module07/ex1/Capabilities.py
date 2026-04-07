from abc import ABC, abstractmethod


class HealCapability(ABC):

    @abstractmethod
    def heal(self):
        ...


class TransformCapability(ABC):

    status = "normal"

    @abstractmethod
    def transform(self):
        ...

    @abstractmethod
    def revert(self):
        ...
