
def physics_calculator():

    while True:
        print("\n===== PHYSICS CALCULATOR =====")
        print("1. Speed")
        print("2. Force")
        print("3. Kinetic Energy")
        print("4. Work Done")
        print("5. Density")

        choice = int(input("Choose an operation (1-5): "))

        if choice == 1:
            distance = float(input("Enter distance (m): "))
            time = float(input("Enter time (s): "))

            speed = distance / time
            print("Speed =", speed, "m/s")

        elif choice == 2:
            mass = float(input("Enter mass (kg): "))
            acceleration = float(input("Enter acceleration (m/s²): "))

            force = mass * acceleration
            print("Force =", force, "N")

        elif choice == 3:
            mass = float(input("Enter mass (kg): "))
            velocity = float(input("Enter velocity (m/s): "))

            kinetic_energy = 0.5 * mass * velocity ** 2
            print("Kinetic Energy =", kinetic_energy, "J")

        elif choice == 4:
            force = float(input("Enter force (N): "))
            distance = float(input("Enter distance (m): "))

            workdone = force * distance
            print("Work Done =", workdone, "J")

        elif choice == 5:
            mass = float(input("Enter mass (kg): "))
            volume = float(input("Enter volume (m³): "))

            density = mass / volume
            print("Density =", density, "kg/m³")

        else:
            print("Invalid choice! Select between 1 and 5.")

        again = input("\nDo you want to continue? (yes/no): ")

        if again.lower() != "yes":
            print("Thank you for using the Physics Calculator!")
            break


physics_calculator()
