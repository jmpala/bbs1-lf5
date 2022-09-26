# Switch impl in python
def switch_test(parameter):
    test = {
        1: "Mathematik",
        2: "Deutsch",
        3: "Informatik",
        4: "Sport"
    }
    print(test.get(parameter, "Invalid"))

switch_test(9)