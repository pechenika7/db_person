class person():

    @classmethod
    def verify_age(cls, age):
        if isinstance(age, int):
            return True
        else:
            return False

    def show_weight(self):
        return self.__weight

    def set_weight(self, w):
        self.__weight = w

    def __init__(self, fio, age, weight, ps):
        self.__fio = fio
        self.__age = age
        self.__weight = weight
        self.__ps = ps