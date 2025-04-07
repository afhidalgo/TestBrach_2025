import utilitiesA as utilA


def main():
    a = 5
    b = 6

    c = utilA.sumaA(a, b)
    print(f"la suma de a + b es: {c}")

    d = utilA.sumaA(c, b)

if __name__ == "__main__":
    main()
