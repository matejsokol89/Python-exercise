def while_loop():
    count = 5
    # counter je na 5
    while count < 50:
        # vrtim dokle god je 5 manje od 50
        count = count + 1
        # ovdje tih 5 incrementam za 1 pa će biti 5,6,7....10,11...15...,30...
        if count % 5 == 0 and count % 3 == 0:
            # provjeravam je li broj djeljiv sa 5 i 3
            print("ovo je djeljivo s 3 i 5")
            print(count)
            # ako je printaj mi taj broj


def for_loop_divide():
    value = 50
    for i in range(5, value + 1):
        if i % 5 == 0 and i % 3 == 0:
            print(i)
