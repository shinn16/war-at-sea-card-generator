from json.encoder import JSONEncoder
from models.alliance import Alliance
from models.nation import Nation

class ModelJsonEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, Nation):
            return o.__dict__
        elif isinstance (o, Unit):
            return o.__dict__
        elif isinstance(o, Alliance):
            return o.value
        return super().default(o)