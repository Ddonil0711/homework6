my_dict = {'Boris': 2000, 'Nicolas': 1845, 'Jhon': 2005}
print(my_dict)
print(my_dict['Boris'])
print(my_dict.get("Anna"))
my_dict.update({'Maria': 2003,
                  'Max': 1999})
print(my_dict)
a = my_dict.pop('Nicolas')
print(a)
print(my_dict)

my_set = { 1, 1, 2, 2, 'a', 'a', 'b', 'b', (1 ,2 ,3)}
print(my_set)
modified_set = {1, 1, 2, 2, 'a', 'a', 'b', 'b', (1, 2, 3,), 43, 24}
modified_set.remove(1)
print(modified_set)