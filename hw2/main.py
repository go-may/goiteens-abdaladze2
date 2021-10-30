my_dict = {
    'test': 1,
    'a': 3,
    'c': 3,
    'b': 3
}

def add_to_dict(dict, key, value = None):
    dict[key] = value
    return dict

def delete_from_dict(dict, key):
    del dict[key]
    return dict

def edit_to_dict(dict, key, value = None):
    dict[key] = value
    return dict

def has_key_is_dict(dict, key):
    return True if dict[key] else False

def print_dict(dict):
    print (dict)

def sort(dict):
    pass

# while True:
#     what = input('Команда: ')
#     if what == 'add':
#         key = input('Ключ: ')
#         value = input('Значение: ')
#         if has_key_is_dict(dict, key):
#             bool_edit =  input('Этот ключ уже существует хотите ли вы изменить его значение ? ')
#             value = input('Новое значение: ')
#             if bool_edit == 'yes':
#                 edit_to_dict(dict, key, value)
#             if bool_edit == 'no':
#                 add_to_dict(dict, key, value)
#         else:
#             add_to_dict(dict, key, value)
#
#     if what == 'delete':
#         key = input('Ключ: ')
#         if has_key_is_dict(dict, key):
#             delete_from_dict(dict, key)
#         else:
#             print ('Такого ключа в словаре не существует')
#     if what == 'edit':
#         key = input('Ключ: ')
#         if has_key_is_dict(dict, key):
#             value = input('Значение: ')
#             edit_to_dict(dict, key, value)
#         else:
#             print ('Такого ключа в словаре не существует')
#     if what == 'is_key':
#         key = input('Ключ: ')
#         print ('Есть' if has_key_is_dict(dict, key) else 'Нету')
#
#     if what == 'show':
#         print_dict(dict)

# 3

count_meets = 0

c_k = ''
c_v = ''

for k, v in my_dict.items():
    if c_k == k: count_meets += 1
    if c_v == v: count_meets += 1

    if c_k != k: c_k = k
    if c_v != v: c_v = v

print (count_meets)

str1 = 'Hello World!'

for x in str1:
    if str1.index(x) % 3 == 0:
        print (x)

# 4

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

for i in my_list:
    if my_list.index(i) % 2 == 1:
        print (i)