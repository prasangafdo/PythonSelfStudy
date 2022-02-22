class Main:

    value = input("Enter 3 names followed by \"-\" for each name")
    name1, name2, name3 = value.split("-")
    print(name1, name2, name3)