#BMI calculator in pounds
#BMI = weight / height squared 

def main():
    
    print("Welcome, to the world renown BMI calculator")
       
    
    print("""
    First, enter your weight?
    """)
    weight = int(input("Please enter your weight"))
        
    
        
        
    
    print("""
    Second, how would you like to enter your height?
    1. Feet and inches
    2. Meters
    3. Centimeters""")
    height = int(input("Please choose a number from the list"))
    if height == 1:
        var = eval(input("Enter feet"))
        var2 = eval(input("Enter inches"))
        y = var * 12 + var2
    elif height ==  2:
        y = input(int("Please enter your height in meters"))
    elif height == 3:    
        y == input(int("Please enter your height in centimeters"))

         
    
            
            


def calculate():
    x, y = main()

    BMI =  "{} / {}*{}". format(x, y, y)
    
main()
        

    
    
        
    

    
    