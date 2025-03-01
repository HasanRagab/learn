# Ensures that a class has only one instance and provides a global point of access to it.
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  
print(obj1 == obj2)  
