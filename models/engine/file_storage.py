import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            to_dump = {}
            for key, value in self.__objects.items():
                to_dump[key] = value.to_dict()
            json.dump(to_dump, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, encoding='utf-8') as f:
                to_load = json.load(f)
                for key, value in to_load.items():
                    self.__objects[key] = type(value)(**value)
        except FileNotFoundError:
            pass
