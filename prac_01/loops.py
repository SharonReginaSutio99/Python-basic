def main():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for j in range(0, 101, 10):
        print(j, end=' ')
    print()

    for k in range(20, 0, -1):
        print(k, end=' ')
    print()

    stars = int(input("Number of stars: "))
    asterisks = ""
    for n in range(stars):
        asterisks += "*"
    print(asterisks)

    asterisks = ""
    for n in range(stars):
        asterisks += "*"
        print(asterisks)


main()
