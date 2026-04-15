price=float(input("Початкова ціна товару: "))
discount=float(input("Знижка (%): "))

final_price=price*(1-discount/100)

print("Ціна після знижки:", round(final_price, 2), "грн")
