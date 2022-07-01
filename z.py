
#Задание5
a = input("Введите предложение:")
b = a.count(" ")
while b < int(5):
        b = a.count(" ")
        if b >= 5:
                print(a[(len(a)//2+1):],a[0:(len(a)//2+1)])
                break
        elif b < 6:
                a = input("Введите предложение:")

#Задание1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
        if i>5:
                print(i)
        else:
                continue

#Задание2
digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
for i in digits:
    print(i/9)

