# Node class
class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None

# Polynomial using Linked List
class Polynomial:
    def __init__(self):
        self.head = None

    def append(self, coeff, power):
        new_node = Node(coeff, power)
        if not self.head or self.head.power < power:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.power >= power:
                current = current.next
            if current.power == power:
                current.coeff += coeff
            else:
                new_node.next = current.next
                current.next = new_node

    def display(self):
        current = self.head
        if not current:
            print("0")
            return
        while current:
            sign = "+" if current.coeff >= 0 else ""
            print(f"{sign}{current.coeff}x^{current.power}", end=" ")
            current = current.next
        print()

    @staticmethod
    def add(p1, p2):
        result = Polynomial()
        a = p1.head
        b = p2.head

        while a and b:
            if a.power == b.power:
                result.append(a.coeff + b.coeff, a.power)
                a = a.next
                b = b.next
            elif a.power > b.power:
                result.append(a.coeff, a.power)
                a = a.next
            else:
                result.append(b.coeff, b.power)
                b = b.next

        while a:
            result.append(a.coeff, a.power)
            a = a.next
        while b:
            result.append(b.coeff, b.power)
            b = b.next

        return result

# Function to get polynomial from user
def get_polynomial_input():
    poly = Polynomial()
    n = int(input("Enter number of terms: "))
    print("Enter each term as: coefficient power")
    for _ in range(n):
        coeff, power = map(int, input("Term: ").split())
        poly.append(coeff, power)
    return poly

# ----------- MAIN PROGRAM -----------
print("Enter Polynomial 1:")
p1 = get_polynomial_input()

print("Enter Polynomial 2:")
p2 = get_polynomial_input()

print("\nPolynomial 1:")
p1.display()

print("Polynomial 2:")
p2.display()

# Addition
result = Polynomial.add(p1, p2)

print("Resultant Polynomial after Addition:")
result.display()
