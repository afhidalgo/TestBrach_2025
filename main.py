import utilitiesA as utilA
import utilitiesB as utilB


def main():
    a = 5
    b = 6

    c = utilA.sumaA(a, b)
    print(f"la suma de a + b es: {c}")

    d = utilB.restaB(a, b)
    print(f"la resta de a + b es: {d}")

if __name__ == "__main__":
    main()
