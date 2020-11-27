# regardless of the entire discussion whether this is a bad or a good design pattern... :p
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class UniqueClass(metaclass=Singleton):
    pass


class AnotherUniqueClass(metaclass=Singleton):
    pass
