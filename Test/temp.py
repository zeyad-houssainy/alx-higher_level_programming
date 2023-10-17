from datetime import datetime
from datetime import timedelta


def my_fct(**kwargs):
    print(f"{kwargs}")


# a_dict = {'name': "zeyad", 'age': 222}
# my_fct(a_dict)  # ({'age': 89, 'name': 'Best'},) - {}
# print("")
# my_fct(*a_dict)  # ('age', 'name') - {}
# print("")
# my_fct(**a_dict)  # () - {'age': 89, 'name': 'Best'}


time_now = datetime.now()
print(time_now)
print(type(time_now))
print(id(time_now))
print("")
time_tomorrow = datetime.now() + timedelta(days=1)
print(time_tomorrow)
temp_dict = {'time now is': time_now, 'time tomorrow is': time_tomorrow}


my_fct(**temp_dict)
