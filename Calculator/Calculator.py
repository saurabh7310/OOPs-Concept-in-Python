# Here we are going to make a Simple Calculator with the help of Object Oriented Programming.

# Parent Class
class Calculator():
    def __init__(self, firstNumber, secondNumber):
        self.firstNumber = firstNumber
        self.secondNumber = secondNumber

    def PrintNumbers(self):
        print("\n-------- Entered Numbers -----------\n")
        print(f"First Number : {self.firstNumber}")
        print(f"Second Number : {self.secondNumber}")

# Child Class
class Operations(Calculator):
    def __init__(self, firstNumber, secondNumber):
        super().__init__(firstNumber, secondNumber)
    
    # Addition
    def Addition(self):
        Operations(firstNumber, secondNumber).PrintNumbers()
        print(f"Addition {firstNumber} + {secondNumber} : {self.firstNumber + self.secondNumber}")

    # Substraction
    def Substraction(self):
        print(f"Substraction {firstNumber} - {secondNumber} : {self.firstNumber - self.secondNumber}")
        
    # Multiplication
    def Multiplication(self):
        print(f"Multiplication {firstNumber} * {secondNumber} : {self.firstNumber * self.secondNumber}")
        
    # Division
    def Division(self):
        print(f"Division {firstNumber} / {secondNumber} : {self.firstNumber / self.secondNumber}")
        
    # Floor
    def Floor(self):
        print(f"Floor {firstNumber} // {secondNumber} : {self.firstNumber // self.secondNumber}")
        
    # Exponential
    def Exponential(self):
        print(f"Exponential {firstNumber} ** {secondNumber} : {self.firstNumber ** self.secondNumber}")
    
    # Modulus
    def Modulos(self):
        print(f"Modulos {firstNumber} % {secondNumber} : {self.firstNumber % self.secondNumber}")
        
if __name__ == '__main__':
    
    while (True): 
        firstNumber = int(input("Enter first Number : "))
        secondNumber = int(input("Enter second Number : "))
    
        print('''Please Choose an Option for Calculations 
            
            1. Press + for Addition.
            2. Press - for Substraction.
            3. Press * for Multiplication.
            4. Press / for Division.
            5. Press // for floor.
            6. Press ** for Exponentioal.
            7. Press % for Exponential.
            8. Press A for All Calculations.''')
        
        choice = input("Choose a key for Calculation : ")
        if choice == "+":
            Operations(firstNumber, secondNumber).Addition()
        elif choice == '-' :
            Operations(firstNumber, secondNumber).Substraction()
        elif choice == '*' :
            Operations(firstNumber, secondNumber).Multiplication()
        elif choice == '/' :
            Operations(firstNumber, secondNumber).Division()
        elif choice == '//' :
            Operations(firstNumber, secondNumber).Floor()
        elif choice == '**' :
            Operations(firstNumber, secondNumber).Exponential()
        elif choice == '%' :
            Operations(firstNumber, secondNumber).Modulos()
        elif choice == 'A':
            Operations(firstNumber, secondNumber).Addition()
            Operations(firstNumber, secondNumber).Substraction()
            Operations(firstNumber, secondNumber).Multiplication()
            Operations(firstNumber, secondNumber).Division()
            Operations(firstNumber, secondNumber).Floor()
            Operations(firstNumber, secondNumber).Exponential()
            Operations(firstNumber, secondNumber).Modulos()
        else:
            print(f"Please Press a Valid Key. Your key is '{choice}'.")
        userChoice = ""
        while((userChoice != "Q" and userChoice !="q") and (userChoice != "C" and userChoice != "c")):
            userChoice = input("Press [Any Key] for Quit and for Continue Press [C or c] : ")
            if (userChoice == "c") or (userChoice == "C"):
                continue
            else:
                print("Thanks for using.")
                quit()