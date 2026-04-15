b = float(input("Білки (г): "))
f = float(input("Жири (г): "))
c = float(input("Вуглеводи (г): "))

calories = b*4+f*9+c*4

print("Загальна кількість калорій:", round(calories, 2), "ккал")
