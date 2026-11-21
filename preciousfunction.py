
while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Speed Calculation")
    print("2. Force Calculation")
    print("3. Work Done Calculation")
    print("4. Density Calculation")
    print("5. Kinetic Energy Calculation")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        distance = float(input("Enter distance (m): "))
        time = float(input("Enter time (s): "))

        if time > 0:
            speed = distance / time
            print("Speed =", speed, "m/s")
        else:
            print("Time must be greater than zero.")

    elif choice == "2":
        mass = float(input("Enter mass (kg): "))
        acceleration = float(input("Enter acceleration (m/s²): "))

        force = mass * acceleration
        print("Force =", force, "N")

    elif choice == "3":
        force = float(input("Enter force (N): "))
        distance = float(input("Enter distance (m): "))

        work_done = force * distance
        print("Work Done =", work_done, "J")

    elif choice == "4":
        mass = float(input("Enter mass (kg): "))
        volume = float(input("Enter volume (m³): "))

        if volume > 0:
            density = mass / volume
            print("Density =", density, "kg/m³")
        else:
            print("Volume must be greater than zero.")

    elif choice == "5":
        mass = float(input("Enter mass (kg): "))
        velocity = float(input("Enter velocity (m/s): "))

        kinetic_energy = 0.5 * mass * velocity ** 2
        print("Kinetic Energy =", kinetic_energy, "J")

    elif choice == "6":
        print("Thank you for using the Physics Calculator!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 6.")
