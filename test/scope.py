def f1():
    scope1 = 1023
    print("id=", id(scope1), "val=", scope1)
    if True:
        scope1 = 10023
        print("id=", id(scope1), "val=", scope1)
    print("id=", id(scope1), "val=", scope1)

f1()
