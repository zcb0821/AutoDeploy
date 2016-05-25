from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
from django.db import models
import json
import datetime


def extended_json_serializer(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime("%Y/%m/%d %H:%M")
    elif isinstance(obj, datetime.date):
        return obj.strftime("%Y/%m/%d")
    else:
        raise TypeError


def model_to_dict(model, fields=None):
    if fields is None:
        fields = model._meta.local_fields
    return {field.attname: model.__dict__.get(field.attname) for field in fields}


class QuerySetJSONEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, models.query.QuerySet):
            return json.dumps([model_to_dict(model) for model in o], default=extended_json_serializer)
        else:
            return super(QuerySetJSONEncoder, self).default(o)


class ListField(models.TextField):
    description = "Stores a python list object"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection, context):
        if value is None or isinstance(value, list):
            return None
        return json.loads(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return json.dumps(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_prep_value(value)