x = [1, 5, 8, 15, 16, 17, 22, 26, 29, 31, 45]
a = [1, 'b', 5, 8, '13', 15, '16', 17, '22', 26, 29, 'abc', 31, 45]
b = [25, 3, 11, 13, 5, 1, 26, 29, 11]
c = "Какое-то очень интересное и длинное предложение! "
#ЗАДАЧА №1
"""
print ("ЗАДАЧА №1↑")
print (sum(x))
#ЗАДАЧА №2
print ("ЗАДАЧА №2")
result = []

for number in a:
    if number in b:
        result.append(number)

print(result)

#ЗАДАЧА №3
print ("ЗАДАЧА №3")
i = 0
result = []
for num in b:
    if i > 3 and i % 2 == 0:
        result.append(num)
    i += 1
print(result)
i += 1
#ЗАДАЧА №4
print ("ЗАДАЧА №4")
c_new = c
c_new = c_new.replace(" ", "")
print(len(c_new))
print (c)
#ЗАДАЧА №5
print ("ЗАДАЧА №5")
v = []
for num in a:
    if type(num) == int:
        v.append(num)
for num in b:
    v.append(num)
v.sort()
print(v)
"""
result_3 = []
for index in range(len(b)):
    if index % 2 == 0 and index > 3:
        result_3.append(b[index])
print(result_3)

print(b[3])

        

