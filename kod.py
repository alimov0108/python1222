import time
a = 0
while True:
    a += 1
    ism = input("Ismingizni kiriting: ")
    fam = input("Familyazni kiriting: ")
    yil = input("tugilgan yilizni kiriting: ")
    parol1 = input("Parolni kiriting: ")
    parol2 = input("Parol2ni kiriting: ")
    print(ism+  fam+  yil)

    if parol1 == "12345":
        print("parol togri")
        break

    elif parol2 == "12345":
        print("parol xato")
        break

    elif parol1 == 3:
        print("siz 3marta xato kod kiritdingiz")
        for x in range(10):
            time.sleep(0.3)
            print(x)
    elif parol2 == 3:
        print("siz 3marta xato kod kiritdingiz")
        for x in range(10):
            time.sleep(0.3)
            print(x)
    elif parol1 == 5:
        print("siz 5marta xato kod kiritdingiz")
        for x in range(30):
            time.sleep(0.3)
            print(x)
    elif parol2 == 5:
        print("siz 5marta xato kod kiritdingiz")
        for x in range(30):
            time.sleep(0.3)
            print(x)