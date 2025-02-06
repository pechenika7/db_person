from person import *
p = person('Иванов Иван Иваныч', 20, 70, 1243432135)
person.verify_age(17)
p.set_weight(75)
print(p.show_weight())