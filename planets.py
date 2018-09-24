# Justin Youn
# CPE 202-1/2
# Lab 0 Parkinson
def weight_on_planets():
    # Prompts user for weight on earth
    userWeight = float(input("What do you weigh on earth? "))
    print()
    # Gets the weight of the user on mars and jupiter
    marsWeight = userWeight * 0.38
    jupiterWeight = userWeight * 2.34
    # Print the final weight statement
    print("On Mars you would weigh "+str(marsWeight) + " pounds.\nOn Jupiter you would weigh "+str(jupiterWeight) + " pounds.")
if __name__ == '__main__':
    weight_on_planets()
