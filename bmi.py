def calculate_bmi(height, weight):

    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height ** 2)
    print("Your bmi is:" + str(bmi))

    if bmi < 18.5:
        print("You are under weight")
        return -1
    elif bmi <= 35.0:
        print("Your are normal weight")
        return 0
    else:
        print("You are overweight")
        return 1


calculate_bmi(weight=57, height=1.73)