import json
import os
from datetime import datetime

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            d = {}
            for key, value in FileStorage.__objects.items():
                d[key] = value.to_dict()
            f.write(json.dumps(d))

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.loads(f.read())
                for key, value in FileStorage.__objects.items():
                    k = key.split('.')
                    FileStorage.__objects[key] = eval(k[0])(**value)
