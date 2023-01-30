import json
import os

class FileStorage:
__file_path = "file.json"
__objects = {}
def all(self):
    return FileStorage.__objects

def new(self, obj):
    FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

def save(self):
    with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
        d = {key: val.to_dict() for key, val in FileStorage.__objects.items()}
        json.dump(d, f)

def reload(self):
    if os.path.exists(FileStorage.__file_path):
        with open(FileStorage.__file_path, encoding="utf-8") as f:
            d = json.load(f)
            for key, val in d.items():
                cls_name, obj_id = key.split(".")
                val["__class__"] = cls_name
                FileStorage.__objects[key] = eval(cls_name)(**val)
