class BaseService(object):
    model = None

    def __init__(self, model_class):
        self.model = model_class

    def get_all(self):
        return self.model.select()

    def get_by_id(self, model_id):
        return self.model.get(self.model.id == model_id)

    def delete_by_id(self, id):
        instance = self.get_by_id(id)
        instance.delete_instance()

    def add(self, data):
        instance = self.model(**data)
        instance.save()
        return instance
