# 1
def registration(login, password):
    file1 = open('l', 'w')
    file1.write(login)
    file1.close()

    file2 = open('p', 'w')
    file2.write(hash_pass(password))
    file2.close()

def hash_pass(password):
    hash = ''
    for p in password:
        hash += p
        if password.index(p) % 2 == 0:
            hash += '%2' + str(len(password))
        if password.index(p) % 2 == 1:
            hash += '%30()' + str(len(p))

    return hash

# 2
count_meets = 0
list2 = []
list1 = [1, 2, 3, 4, 5, 5, 2, 3, 5, 8]

for x in list1:
    try:
        if list2[list1.index(x)]:
            count_meets += 1
    except IndexError:
        list2.append(x)

print (count_meets)

# 3
def find_top_3_words():
    file = open('file', 'r')
    top_words = ['He', 'Wo', '!']

    for x in top_words:
        if x in file.read():
            print (x)

find_top_3_words()