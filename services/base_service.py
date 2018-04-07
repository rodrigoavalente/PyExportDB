class BaseService(object):
    model = None

    def __init__(self, model_class):
        self.model = model_class

    def get_all(self, order_by_field=None):
        if order_by_field:
            self.model.select(getattr(self.model, order_by_field))
        return self.model.select()

    def get_by_id(self, model_id):
        return self.model.get_by_id(model_id)

    def get_by_field(self, field, value):
        return self.model.get(getattr(self.model, field) == value)

    def delete_by_id(self, model_id):
        return self.model.delete_by_id(model_id)

    def add(self, data):
        instance = self.model(**data)
        instance.save()
        return instance

    def update(self, model_id, data):
        return self.model.update(**data).where(self.model.id == model_id).execute()
