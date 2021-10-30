# 1
str1 = 'Hi'
str2 = 'World'

search = 'o'
is_found = False
for a in str1:
    if a == search:
        print (a)
        is_found = True
        break

if is_found != True:
    for b in str2:
        if b == search:
            print(b)
            is_found = True
            break

# 2
unique = []

str3 = 'Hello World!'
for x in str3:
    if x in unique:
        pass
    else:
        unique.append(x)

print (unique)

# 3
def get_max_in_list(list):
    max = 0
    for x in list:
        if max < x:
            max = x
    return max

list = [1, 3, 8, 30, 20]
print (get_max_in_list(list))