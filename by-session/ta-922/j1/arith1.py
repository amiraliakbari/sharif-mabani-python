a = float(raw_input())
b = int(raw_input())
c = int(raw_input())

delta = ((b * b) - 4 * a * c) ** 0.5

x1 = (-b + delta ) / (2 * a)
x2 = (-b - delta ) / (2 * a)

print x1, x2
