#a simple bmi calculator using the python language 

#method to calculate the bmi using the weight and height inputs 
def cal_bmi(WEIGHT, HEIGHT):
    #try block to throw if any exception raises like divide by zero 
    try:
        #type conversion from string to float to avoid errors
        WEIGHT = float(WEIGHT)
        HEIGHT = float(HEIGHT)
        #formula to calculate the bmi 
        bmi=WEIGHT/(HEIGHT ** 2)

        return bmi
    #except block to handle the error 
    except ValueError:
        return None

#method to take the input from user and check where it is a legitmit one 
def get():
    while True: #infinite loop till we get a correct input 
        #prompt for user to give the inputs 
        WEIGHT = input("Enter your WEIGHT in kilograms: ")
        HEIGHT = input("Enter your HEIGHT in meters: ")

        #conditional statements to check wheather the user input is correct or not
        #using the isnumeric methods and the decimal values 
        if WEIGHT.isnumeric() or (WEIGHT.replace('.', '', 1).isdigit() and WEIGHT.count('.') <= 1):
            if HEIGHT.isnumeric() or (HEIGHT.replace('.', '', 1).isdigit() and HEIGHT.count('.') <= 1):
                return WEIGHT, HEIGHT
            else:
                print("Invalid HEIGHTt input. Please enter a valid numeric value.")
        else:
            print("Invalid WEIGHT input. Please enter a valid numeric value.")

#method to classify the category based on the bmi 
def classify(bmi):

    #conditional statements to dvide into a correct group \

    if bmi < 18.5: ##group of underweight 
        return "Under WEIGHT, please put on some WEIGHT to maintain good bmi"
    
    elif 18.5 <= bmi < 25:#group of normal weight 
        return "Normal WEIGHT, your bmi is perfect try to maintain"
    
    elif 25 <= bmi < 30:#group of over weigth 
        return "Over WEIGHT, please put off some WEIGHT"
    
    else:#finally obese 
        return "Obese, immediate action should be taken for the WEIGHT reduction"

#main function consisting all the actions 
def main():
    print("BMI CALCULATOR")
    while (1):
        WEIGHT, HEIGHT = get()
        bmi = cal_bmi(WEIGHT, HEIGHT)
        if bmi is not None:
            print(f"Your BMI is: {bmi:.2f}")
            print(f"you are in category of:{classify(bmi)}")
            exit()
        else: ##returns the error message if input is not valid 
            print("Invalid input. Please enter valid numeric values for WEIGHT and HEIGHTt.")

# 1.)intially we give wrong inputs to check the code working with the wrong inputs 
# 2.)we provide the right inputs for the code to give us the result we need 
# 3.)we finally try to raise an exception with our inputs 

main()


