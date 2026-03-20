buyer = input("Enter Buyer Name: ")
apple_price = float(input("Enter Apple price per kg: "))
apple_qty = float(input("Enter Apple Quantity in kg: "))
orange_price = float(input("Enter Orange price per kg: "))
orange_qty = float(input("Enter Orange Quantity in kg: "))

apple_total = apple_price * apple_qty
apple_gst = apple_total * 0.12
apple_with_gst = apple_total + apple_gst

orange_total = orange_price * orange_qty
orange_gst = orange_total * 0.05
orange_with_gst = orange_total + orange_gst

total = apple_with_gst + orange_with_gst

print(f"\nBuyer Name: {buyer}")
print("-" * 74)
print("| Item Code  | Price/Unit | # unit | Price |    GST     | Total w/ GST |")
print("-" * 74)
print(f"|   Apple    |   Rs {apple_price:.0f}   |  {apple_qty}  | Rs {apple_total} |  Rs {apple_gst}  | Rs {apple_with_gst}  |")
print(f"|   Orange   |   Rs {orange_price:.0f}   | {orange_qty}  | Rs {orange_total} |  Rs {orange_gst}   | Rs {orange_with_gst}  |")
print("-" * 74)
print(f"Total                                                        ₹ {total:.2f}")
print(f"Total Round                                                  ₹ {round(total):.2f}")
print("-" * 74)
