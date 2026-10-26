
def show():
    print("A:", A, "B:", B, "C:", C)
    print()


def towerOfHanoi(n, src, aux, dest):
    if n == 1:
        dest.append(src.pop())
        show()
        return

    towerOfHanoi(n - 1, src, dest, aux)

    dest.append(src.pop())
    show()

    towerOfHanoi(n - 1, aux, src, dest)


n = int(input("Enter number of disks: "))

A = list(range(n, 0, -1))
B = []
C = []

print("Initial state:")
show()

towerOfHanoi(n, A, B, C)

print("Final state:")
show()

