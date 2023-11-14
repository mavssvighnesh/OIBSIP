#PYTHON PROGRAM TO GENERATE RANDOM PASSWORD IN A COMMAND LINE INTERFACE 

#ASKS THE USER TO CONFIGURE THEIR PASSWORD FEATURES LIKE DO THEY WANT SYMBOLS LETTERS NUMBERS AND CUSTOMIZE IT 
#FINALLY ALSO ASKS WHEATHER THE USER IS SATISFIED OF THE PASSWORD GENERATED OR NOT IF NOT WE TRY TO RECONFIGURE THE FEATURES AND RE GENERATE IT 

#Importing the requried module like random for randomization of the characters and string for string functions
import random
import string


#Method to generate the password with the required specifications 
def create_passcode(length,letters,numbers,symbols):
    password = '' #null string to add the random characters 

    #Includes the letters in the passcode 
    if letters:
        password+=string.ascii_letters

    #Includes the numbers in the passcode
    if numbers:
        password+=string.digits
    
    #Include the symbols in the passcode
    if symbols:
       password+=string.punctuation

    #Checks that atleast one type is selected or not 
    if not any([letters,numbers,symbols]):
        print("YOU SHOULD SELECT ATLEAST ONE TYPE TO GENERATE A PASSWORD")
        return None

    #add the randome characters to the passcode with in the given range 
    passcode=''.join(random.choice(password)for _ in range(length))
    return passcode

#Method to take the specification inputs from the user 
def get():
    #Iterates until the length input is sucess 
    while True:
        #try block to throw if any exception arises 
        try:

            #Takes the input of specification what we want length,letters,numbers,symbols
            length = int(input("ENTER THE PASSWORD LENGTH YOU WANT: "))
            letters = input("DO YOU WANT TO INCLUDE LETTERS? (yes/no):  ").lower()=="y"
            numbers = input("DO YOU WANT TO INCLUDE NUMBERS? (yes/no):  ").lower()=="y"
            symbols = input("DO YOU WANT TO INCLUDE SYMBOLS(yes/no):  ").lower()=="y"

            #Check if the length of the password requried is a valid input 
            if length <= 0:
                print("PASSWORD LENGHT SHOULD BE VALID POSITIVE NUMERIC")
                continue
            return length,letters,numbers, symbols
        
        #Throws the exception if the length of the password is not valid 
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER OF PASSWORD LENGTH")

#Main method which encapsulates all the method callings 
def main():
  print("WELCOME TO RANDOM PASSWORD GENRATOR")
  #Iterates until the type input is sucess 
  while(1):
     length,letters,numbers,symbols = get()
     passcode=create_passcode(length,letters,numbers,symbols)

    #If we get a passcode as the value we print 
     if passcode:
        print(f"Generated password: {passcode}")

        #Checks wheather the customer is satisfied with the password or not 
         #uses the startswith method to make a boolean output
        satisfied=input("ARE U SATISFIED WITH THE GENERATED PASSWORD? (yes/no): ").lower().startswith('y')

        if(satisfied==True): #If satisfied exits the program 
            exit()
        else: #If not satisfied ask for the new configuration
            print("RE ENTER THE CONFIGURATION YOU WANT")
            pass       
     else:
       print("ENTER THE VALID INPUT FOR TYPE SELECTION")

#Calling the main method      
main()
