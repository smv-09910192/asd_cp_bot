from abc import ABC, abstractmethod

class Entity(ABC):

    @abstractmethod
    def json_serialize(self):
        pass