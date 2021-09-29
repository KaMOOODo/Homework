"""A singleton is a class that allows only a single instance of itself to be created and
gives access to that created instance.
Implement singleton logic inside your custom class using a method to initialize class instance."""


class Singleton:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class Sun:
    @staticmethod
    def inst():
        return Singleton



p = Sun.inst()
f = Sun.inst()
print(p is f)
# True