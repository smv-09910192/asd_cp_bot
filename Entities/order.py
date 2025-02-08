import json

class Order:
     def __init__(self):
        pass
     
     def set_user_name(self, username):
         self.UserName = username;

     def set_user_phone(self, phone):
         self.Phone = phone;

     def set_invertor(self, invertor):
         self.Invertor = invertor;
     
     def set_battery(self, battery):
         self.Battery = battery;
     
     def json_serialize(self):
        return json.dumps(self, cls=InvertorEncoder)
     
class InvertorEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Order):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)