while True:
    try:
        n = int(input("The amount of money to be exchanged: "))

        if n <= 0:
            print(
                "The amount of money to be exchanged must be positive. Try again!"
            )
            continue

        x, y, z = map(
            int,
            input("Enter three denominations: ").split()
        )

        if (
            x == y
            or y == z
            or x == z
            or x <= 0
            or y <= 0
            or z <= 0
        ):
            print(
                "The denominations must be positive and distinct. Try again!"
            )
            continue

        x, y, z = sorted([x, y, z], reverse=True)

        found = False

        for i in range(n // x + 1):
            for j in range(n // y + 1):

                remaining = n - i * x - j * y

                if remaining >= 0 and remaining % z == 0:
                    h = remaining // z

                    print(
                        f"{i} coins of {x}, "
                        f"{j} coins of {y}, "
                        f"{h} coins of {z}"
                    )

                    found = True

        if not found:
            print("No solution exists")

        break

    except ValueError:
        print("Enter valid values")