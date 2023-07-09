import collections

class EntityMeta(type):

    @classmethod
    def __prepare__(cls, name, bases):
        return collections.OrderedDict()

    def __init__(scls, name, bases, attr_dict):
        for key, attr in attr.dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)

class Entity(metaclass=EntityMeta):
    """Business entity with validated fields"""

