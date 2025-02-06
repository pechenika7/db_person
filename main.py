from person import *
p = person('Иванов Иван Иваныч', 20, 70, 1243432135)
print(person.verify_age(17))
print(person.verify_weight('45'))
print(person.verify_fio('a b'))
print(person.verify_ps('1111 222222'))
p.set_weight(75)
print(p.show_weight())