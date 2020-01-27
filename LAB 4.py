#LAB 4
choice = 0
while choice != "0":
    print("Select your Desired formula")
    print(" ")
    print("[1] Gravitation Force, F")
    print("[2] Charles Law ")
    print("[Q] to quit exit.")
    print(" ")
    choice = input("Choose your ideal Formula: ")
    print(" ")
    if choice == "1":
        print("~~You chose the formula for Gravitational Force~~")
        print(" ")
        print("Gravitational Force=(-Gravitational Constant * Mass of First Object * Mass of Second Object)/Distance Between two Objects Squared")
        print(" ")
        print("[1] Mass of the First Object")
        print("[2] Mass of the Second Object ")
        print("[3] Gravitational Force")
        print("[4] Distance between two Objects")
        print("[B] Go back to formula selection.")
        print(" ")
        unk1 = input("Choose an unknown variable: ")
        print(" ")

        if unk1 == "1":
            m2 = float(input("Give the weight of the Second  Object "))
            d  = float(input("Give the Squared Distance between two objects  "))
            GravForce = float(input("Give the Value of Gravitational Force"))
            print(" ")
            G = ("Gravitational Constant is 0.000000000067")
            Ans = (((GravForce * d ) )/(G * m2))
            print("The Gravitational Force is", Ans, "KG")
            print(" ")
            print(" ")
	
	elif unk1 == "2":
            m1 = float(input("Give the weight of the First Object "))
            d  = float(input("Give the Squared Distance between two objects  "))
            GravForce = float(input("Give the Value of Gravitational Force"))
            print(" ")
            G = ("Gravitational Constant is 0.000000000067")
            Ans = (((GravForce * d ) )/(G * m1))
            print("The Gravitational Force is", Ans, "KG" )
            print(" ")
            print(" ")

	elif unk1 == "3":
            m1 = float(input("Give the weight of the First Object in KG "))
	    m2 = float(input("Give the weight of the Second Object in KG"))
            d  = float(input("Give the Squared Distance between two objects  "))
            print(" ")
            G = ("Gravitational Constant is 0.000000000067")
            Ans = (((GravForce * m1 *m2 )/(d)))
            print("The Gravitational Force is", Ans, "KG" )
            print(" ")
            print(" ")
	

	elif unk1 == "4":
            m1 = float(input("Give the weight of the First  Object "))
	    m2 = float(input("Give the weight of the Second  Object "))
            GravForce = float(input("Give the Value of Gravitational Force"))
            print(" ")
            G = ("Gravitational Constant is 0.000000000067")
            Ans = ((G * m1 * m2) % GravForce))
            print("Distance Between two object is", Ans,"kg" )
            print(" ")
            print(" ")

     elif choice == "2"

        print("~ Formula for Charles Law~")
        print(" ")
        print("Volume 1/ Temperature 1 = Volume 2/ Temperature 2")
        print(" ")
        print("[1] Volume 1")
        print("[2] Temperature 1")
        print("[3] Volume 2")
        print("[4] Temperature 2")
        print("[B] Go back to formula selection.")
        print(" ")
        unk2 = input("Choose an unknown variable:")
        print(" ")

        if unk2 == "1":
	    print("To Find the answer for Volume 1")
            t1 = float(input("Please put the value of temperature 1 in kelvin "))
            t2 = float(input("Please put the value of temperature 2 in kelvin "))
            v2 = float(input("Please put the value of volume 2 "))
            print(" ")
            Ans2 = ((t1 * v2) % (t2))
            print("The value of v1 ", Ans2, )
            print(" ")
            
        elif unk2 == "2":
	    print("To Find the answer for Temperature 1")
            t2 = float(input("Please put the value of temperature 2 in kelvin "))
            v1 = float(input("Please put the value of volume 1 "))
	    v2 = float(input("Please put the value of volume 2 "))
            print(" ")
            Ans2 = ((v1 * t2) % (v2))
            print("The value of t1 in kelvin", Ans2, "K")
            print(" ")

        elif unk2 == "3":
	    print("To Find the Answer for Volume 2")
            t1 = float(input("Please put the value of temperature 1 in kelvin "))
            t2 = float(input("Please put the value of temperature 2 in kelvin "))
            v1 = float(input("Please put the value of volume 1 "))
            print(" ")
            Ans2 = ((v1 * t2) % (t1))
            print("The value of v1 ", Ans2, )
            print(" ")

        elif unk2 == "4":
           print("To Find the answer for Temperature 2")
            t2 = float(input("Please put the value of temperature 2 in kelvin "))
            v1 = float(input("Please put the value of volume 1 "))
	    v2 = float(input("Please put the value of volume 2 "))
            print(" ")
            Ans2 = ((v2 * t1) % (v1))
            print("The value of t1 in kelvin", Ans2, "K")
            print(" ")

            
    any = input("Press any key to continue...")
    print(" ")
            




