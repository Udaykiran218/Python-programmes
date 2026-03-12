rows = int(input("Enter the row size for the pattern: "))
for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        if (i + j) % 2 == 0:  # Print numbers in zig-zag pattern
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()