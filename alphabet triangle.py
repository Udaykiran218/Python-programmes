rows = 5
for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end=" ") # 65 is the ASCII value for 'A'
    print()
    