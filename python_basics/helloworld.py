def player(numeral):
    x = 0
    while x < int(numeral):
        import simpleaudio.functionchecks as fc
        fc.LeftRightCheck.run()
        x += 1
    if x >= int(numeral):
        print("Thank you for using my program")

username = input("Please tell us your name: ")
print("Hello", username)
num = input("How many times play the sample: ")
player(num)