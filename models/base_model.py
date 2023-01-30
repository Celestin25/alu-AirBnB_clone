import models.engine.file_storage

storage = models.engine.file_storage.FileStorage()

class BaseModel:
    ...

    def save(self):
        """Calls save method of storage and update updated_at attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def __init__(self, *args, **kwargs):
        ...
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
