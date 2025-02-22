import json

from Entities.Entity import Entity

class Invertor(Entity):

    def __init__(self, id, name, price, link):
        self.Id = int(id)
        self.Name = name
        self.Price = price
        self.Link = link
        pass
    
    def json_serialize(self):
        return json.dumps(self, cls=InvertorEncoder)
    
class InvertorEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Invertor):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)