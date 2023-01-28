import json

class FileStorage:
    file_path = 'file.json'
    objects = {}

    @classmethod
    def all(cls):
        return cls.objects

    @classmethod
    def new(cls, obj):
        key = f'{obj.__class__.__name__}.{obj.id}'
        cls.objects[key] = obj

    @classmethod
    def save(cls):
        object_dict = {}
        for obj in cls.objects:
            object_dict[obj] = cls.objects[obj].to_dict()
        with open(cls.file_path, 'w') as file:
            json.dump(object_dict, file)

    @classmethod
    def reload(cls):
        try:
            with open(cls.file_path) as file:
                serialized_content = json.load(file)
                for item in serialized_content.values():
                    class_name = item['__class__']
                    cls.new(eval(class_name + "(**" + str(item) + ")"))
        except FileNotFoundError:
            pass
