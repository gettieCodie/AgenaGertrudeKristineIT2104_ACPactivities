from Capybara import Capybara

capy1 = Capybara("Jenrick", "M",20)
capy2 = Capybara("Trisha", "F",20)
capy3 = Capybara("Rico", "M",20)

capys = [capy1, capy2, capy3]

while (True):
    print()
    test = int(input("Enter the test case number (1-3): "))
    if 1<= test <=3:
        chosen = capys[test -1]
        print(f"Test case {test}: Name: {chosen.name}, Gender: {chosen.gender}, Age: {chosen.age} years old")

    else:
        print("Invalid test case number. Please enter a number between 1 and 3.")

