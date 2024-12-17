pattern_size = int(input("Enter the size of the pattern: "))
i = 0
while i < pattern_size:
    for j in range(0, pattern_size):
        print("*", end="")
    print()
    i += 1
