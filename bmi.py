def calculate_bmi(height, weight):

    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height ** 2)
    print("Your bmi is:" + str(bmi))

    if bmi < 18.5:
        print("You are under weight")
        return bmi, -1
    elif bmi <= 25.0:
        print("Your are normal weight")
        return bmi, 0
    else:
        print("You are overweight")
        return bmi, 1


if __name__ == "__main__":
    calculate_bmi(weight=57, height =1.73)