class person():

    @classmethod
    def verify_age(cls, age):
        if isinstance(age, int):
            return True
        else:
            return False

    @classmethod
    def verify_weight(cls, weight):
        if isinstance(weight, int):
            return True
        else:
            return False

    @classmethod
    def verify_fio(cls, fio):
        return len(fio.split()) == 3

    @classmethod
    def verify_ps(cls, ps):
        list_ = ps.split()
        try:
            return len(list_[0]) == 4 and isinstance(int(list_[0]), int) and len(list_[1]) == 6 and isinstance(int(list_[1]), int)
        except:
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