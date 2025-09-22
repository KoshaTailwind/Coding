a_input = input("Введите a: ")
b_input = input("Введите b: ")
c_input = input("Введите c: ")
a = float(a_input)
b = float(b_input)
c = float(c_input)
D = b**2 - 4*a*c
if D >0:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print(f"Уравнение имеет два корня: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b/(2*a)
    print(f"Уравнение имеет один корень: x = {x}")
else:
    print("Уравнение не имеет корней")
