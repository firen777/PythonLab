# set and tuple is immutable, unordered

set1 = {1,2,3,4,5,6,10,11,1}

print(set1) #{1, 2, 3, 4, 5, 6, 10, 11}

if 1 in set1:
    print(True)

for e in set1:
    print(e)

# dictionary (hashmap?)

dic1 = {"a":1, "b":2, "c":3, 144:"d"}
print(dic1)
print(dic1['a'])
print(dic1[144])

print(dic1.items)
print(dic1.items())

for key, val in dic1.items():
    print(str(key) + "///:\\\\\\" + str(val))