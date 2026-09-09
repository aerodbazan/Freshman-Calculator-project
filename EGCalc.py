#engineering calculator
print("\033[32m")  # Set text color to green
print("""
╔══════════════════════════════════╗
║------Engineering Calculator------║
╚══════════════════════════════════╝
""")
#User input for type/Beginning screen
option = input("----What will you calculate?----\n[1]Force\n[2]Velocity\n[3]Acceleration\n[4]Work\n[5]Power\n[6]Pressure\n[7]Density\n[8]Unit Conversions\n[9]Quit: ").lower()
#-------Functions and Error Handling--------
def calculate_force():
        try:
            mass = float(input("Enter mass in kg: "))
            acceleration = float(input("Enter acceleration in m/s^2: "))
            force = mass * acceleration
            print(f"\nThe force is {force:.2f} N\n")
        except:
            print("\nInvalid input, please enter numeric values.\n")

def calculate_velocity():
        try:
            distance = float(input("Enter distance in meters: "))
            time = float(input("Enter time in seconds: "))
            velocity = distance / time
            print(f"\nThe velocity is {velocity:.2f} m/s\n")
        except:
            print("\nInvalid input, please enter numeric values.\n")

def calculate_acceleration():
        try:
            initial_velocity = float(input("Enter initial velocity in m/s: "))
            final_velocity = float(input("Enter final velocity in m/s: "))
            time = float(input("Enter time in seconds: "))
            acceleration = (final_velocity - initial_velocity) / time
            print(f"\nThe acceleration is {acceleration:.2f} m/s^2\n")
        except:
            print("\nInvalid input, please enter numeric values.\n")

def calculate_work():
        try:
            force = float(input("Enter force in N: "))
            displacement = float(input("Enter displacement in meters: "))
            work = force * displacement
            print(f"\nThe work done is {work:.2f} J\n")
        except:
            print("\nInvalid input, please enter numeric values.\n")

def calculate_power():
        try:
            work = float(input("What is the work done in J: "))
            time = float(input("What is the time? "))
            power = work / time
            print(f"\nThe power is {power:.2f} W\n")
        except:
            print("\nInvalid input, please enter numeric values.\n")

def calculate_pressure():
        try:
            force = float(input("Enter force in N: "))
            area = float(input("Enter area in m^2: "))
            pressure = force / area
            print(f"\nThe pressure is {pressure:.2f} Pa\n")
        except:
            print("\nInvalid input, please enter numeric values.\n")

def calculate_density():
        try:
            mass = float(input("Enter mass in kg: "))
            volume = float(input("Enter volume in m^3: "))
            density = mass / volume
            print(f"\nThe density is {density:.2f} kg/m^3\n")
        except:
            print("\nInvalid input, please enter numeric values.\n")
def calculate_unit_conversions():
        try:
            option2 = input("\nWhat unit conversion type would you like to do? Length, Mass, Force? ").lower()
            if option2 == "length":
                length_conversion()
            elif option2 == "mass":
                mass_conversion()
            elif option2 == "force":
                force_conversion()
            else:
                print("\nInvalid option, please pick again.\n")
        except:
            print("\nInvalid input, please enter a valid option.\n")
#----Nested function for unit conversions----
def length_conversion():
                    try:
                        length_option = input("\nWhat length conversion would you like to do? [1]Meters to Feet, [2]Feet to Meters, [3]Inches to Centimeters, [4]Centimeters to Inches: ").lower()
                        if length_option == "1" or length_option == "meters to feet":
                            meters = float(input("Enter length in meters: "))
                            feet = meters * 3.28084
                            print(f"\n{meters:.2f} meters is equal to {feet:.2f} feet\n")
                        elif length_option == "2" or length_option == "feet to meters":
                            feet = float(input("Enter length in feet: "))
                            meters = feet / 3.28084
                            print(f"\n{feet:.2f} feet is equal to {meters:.2f} meters\n")
                        elif length_option == "3" or length_option == "inches to centimeters":
                            inches = float(input("Enter length in inches: "))
                            centimeters = inches * 2.54
                            print(f"\n{inches:.2f} inches is equal to {centimeters:.2f} centimeters\n")
                        elif length_option == "4" or length_option == "centimeters to inches":
                            centimeters = float(input("Enter length in centimeters: "))
                            inches = centimeters / 2.54
                            print(f"\n{centimeters:.2f} centimeters is equal to {inches:.2f} inches\n")
                        else:
                            print("\nInvalid option, please pick again.\n")
                    except:
                        print("\nInvalid input, please enter numeric values.\n")              
def mass_conversion():
                    try:
                        mass_option = input("\nWhat mass conversion would you like to do? [1] Kilograms to Pounds, [2] Pounds to Kilograms, [3] Grams to Ounces, [4] Ounces to Grams: ").lower()
                        if mass_option == "1" or mass_option == "kilograms to pounds":
                            kilograms = float(input("Enter mass in kilograms: "))
                            pounds = kilograms * 2.20462
                            print(f"\n{kilograms:.2f} kilograms is equal to {pounds:.2f} pounds\n")
                        elif mass_option == "2" or mass_option == "pounds to kilograms":
                            pounds = float(input("Enter mass in pounds: "))
                            kilograms = pounds / 2.20462
                            print(f"\n{pounds:.2f} pounds is equal to {kilograms:.2f} kilograms\n")
                        elif mass_option == "3" or mass_option == "grams to ounces":
                            grams = float(input("Enter mass in grams: "))
                            ounces = grams * 0.035274
                            print(f"\n{grams:.2f} grams is equal to {ounces:.2f} ounces\n")
                        elif mass_option == "4" or mass_option == "ounces to grams":
                            ounces = float(input("Enter mass in ounces: "))
                            grams = ounces / 0.035274
                            print(f"\n{ounces:.2f} ounces is equal to {grams:.2f} grams\n")
                        else:
                            print("\nInvalid option, please pick again.\n")
                    except:
                        print("\nInvalid input, please enter numeric values.\n")  
def force_conversion():
                    try:
                        force_option = input("\nWhat force conversion would you like to do? [1] Newtons to Pounds, [2] Pounds to Newtons: ").lower()
                        if force_option == "1" or force_option == "newtons to pounds":
                            newtons = float(input("Enter force in newtons: "))
                            pounds = newtons * 0.224809
                            print(f"\n{newtons:.2f} newtons is equal to {pounds:.2f} pounds\n")
                        elif force_option == "2" or force_option == "pounds to newtons":
                            pounds = float(input("Enter force in pounds: "))
                            newtons = pounds / 0.224809
                            print(f"\n{pounds:.2f} pounds is equal to {newtons:.2f} newtons\n")
                        else:
                            print("\nInvalid option, please pick again.\n")
                    except:
                        print("\nInvalid input, please enter numeric values.\n")            

while option != "quit" and option != "9":
    
#-------Conditionals--------
    if option == "force" or option == "1":
        calculate_force()

    elif option == "velocity" or option == "2":
        calculate_velocity()

    elif option == "acceleration" or option == "3":
        calculate_acceleration()

    elif option == "work" or option == "4":
        calculate_work()

    elif option == "power" or option == "5":
        calculate_power()

    elif option == "pressure" or option == "6":
        calculate_pressure()

    elif option == "density" or option == "7":
        calculate_density()

    elif option == "unit conversions" or option == "8":
        calculate_unit_conversions()

    else:
        print("\nInvalid option please pick again.\n")
    print("""
╔══════════════════════════════════╗
║------Engineering Calculator------║
╚══════════════════════════════════╝
""")

    option = input("----What will you calculate?----\n[1]Force\n[2]Velocity\n[3]Acceleration\n[4]Work\n[5]Power\n[6]Pressure\n[7]Density\n[8]Unit Conversions\n[9]Quit: ").lower()

print("Calculator closed, come again!")
