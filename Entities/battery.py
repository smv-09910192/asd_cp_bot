import json

from Entities.Entity import Entity

class Battery(Entity):

    def __init__(self, id, name, price, link):
        self.Id = int(id),
        self.Name = name
        self.Price = price
        self.Link = link
        pass

    def json_serialize(self):
        return json.dumps(self, cls=BatteryEncoder)

class BatteryEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Battery):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)